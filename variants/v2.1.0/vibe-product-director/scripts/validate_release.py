#!/usr/bin/env python3
"""Validate source and built release without mutating either."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

NAME = "vibe-product-director"
VERSION = "2.1.0"
ALLOWED_TOP = {"SKILL.md", "README.md", "CHANGELOG.md", "manifest.json", "agents", "references", "assets", "evals", "scripts"}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("SKILL.md frontmatter is missing or malformed")
    raw = text.split("\n---\n", 1)[0][4:]
    if yaml:
        data = yaml.safe_load(raw)
    else:
        data = dict(line.split(":", 1) for line in raw.splitlines() if ":" in line)
    if data.get("name") != NAME or not str(data.get("description", "")).strip():
        raise ValueError("SKILL.md must have the expected name and a non-empty description")
    return data


def validate_links(skill_dir: Path) -> None:
    for file in skill_dir.rglob("*.md"):
        text = file.read_text(encoding="utf-8-sig")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#", "{{")):
                continue
            decoded = target.replace("%20", " ")
            if not (file.parent / decoded).resolve().exists():
                raise ValueError(f"Broken relative link in {file.relative_to(skill_dir)}: {target}")


def validate_evals(skill_dir: Path) -> None:
    trigger = skill_dir / "evals/trigger-cases.csv"
    with trigger.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    positives = sum(row["should_trigger"].strip().lower() == "true" for row in rows)
    negatives = sum(row["should_trigger"].strip().lower() == "false" for row in rows)
    if positives < 14 or negatives < 8 or len({r["id"] for r in rows}) != len(rows):
        raise ValueError(f"Trigger eval coverage invalid: {positives} positive / {negatives} negative")
    scenarios = []
    for line_no, line in enumerate((skill_dir / "evals/behavior-scenarios.jsonl").read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.strip():
            try:
                scenarios.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL line {line_no}: {exc}") from exc
    if len(scenarios) != 20 or len({s["id"] for s in scenarios}) != 20:
        raise ValueError(f"Expected exactly 20 unique behavior scenarios, found {len(scenarios)}")


def validate_manifest(skill_dir: Path) -> None:
    manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("name") != NAME or manifest.get("version") != VERSION:
        raise ValueError("Manifest name/version mismatch")
    actual = {
        p.relative_to(skill_dir).as_posix(): p
        for p in skill_dir.rglob("*")
        if p.is_file() and p.name != "manifest.json"
    }
    listed = {item["path"]: item for item in manifest.get("files", [])}
    if set(actual) != set(listed) or manifest.get("file_count") != len(actual):
        raise ValueError("Manifest coverage does not match source files")
    for rel, path in actual.items():
        data = path.read_bytes()
        if listed[rel]["sha256"] != digest(data) or listed[rel]["bytes"] != len(data):
            raise ValueError(f"Manifest hash/size mismatch: {rel}")


def validate_zip(zip_path: Path, skill_dir: Path) -> None:
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        if not names or any(PurePosixPath(n).is_absolute() or ".." in PurePosixPath(n).parts for n in names):
            raise ValueError("ZIP contains an unsafe path")
        if {PurePosixPath(n).parts[0] for n in names} != {NAME}:
            raise ValueError("ZIP must contain exactly one top-level directory")
        expected = {f"{NAME}/{p.relative_to(skill_dir).as_posix()}" for p in skill_dir.rglob("*") if p.is_file()}
        if set(names) != expected:
            raise ValueError("ZIP entries do not exactly match the source release")
        for name in names:
            rel = Path(*PurePosixPath(name).parts[1:])
            if archive.read(name) != (skill_dir / rel).read_bytes():
                raise ValueError(f"ZIP byte mismatch: {name}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--zip", dest="zip_path", type=Path)
    parser.add_argument("--standalone", type=Path)
    args = parser.parse_args()
    errors: list[str] = []
    skill_dir = args.skill_dir.resolve()
    checks = []
    try:
        unknown = sorted(p.name for p in skill_dir.iterdir() if p.name not in ALLOWED_TOP)
        if unknown:
            raise ValueError(f"Unknown top-level entries: {', '.join(unknown)}")
        frontmatter(skill_dir / "SKILL.md")
        config = yaml.safe_load((skill_dir / "agents/openai.yaml").read_text(encoding="utf-8")) if yaml else {}
        if yaml and config.get("policy", {}).get("allow_implicit_invocation") is not True:
            raise ValueError("Implicit invocation must be enabled")
        validate_links(skill_dir)
        validate_evals(skill_dir)
        validate_manifest(skill_dir)
        checks.extend(["frontmatter", "openai.yaml", "links", "eval formats/counts", "manifest coverage/hashes"])
        if args.zip_path:
            validate_zip(args.zip_path.resolve(), skill_dir)
            checks.append("ZIP structure/path safety/bytes")
        if args.standalone:
            if args.standalone.resolve().read_bytes() != (skill_dir / "SKILL.md").read_bytes():
                raise ValueError("Standalone SKILL copy differs from source SKILL.md")
            checks.append("standalone SKILL byte identity")
    except (OSError, ValueError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        errors.append(str(exc))
    if errors:
        for error in errors:
            print(f"VALIDATION FAILED: {error}", file=sys.stderr)
        return 1
    print("Validation passed: " + ", ".join(checks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
