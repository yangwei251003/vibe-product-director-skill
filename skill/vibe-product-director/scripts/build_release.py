#!/usr/bin/env python3
"""Build a deterministic, allowlisted Vibe Product Director release."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import zipfile

NAME = "vibe-product-director"
VERSION = "2.2.0"
ALLOWED_TOP = {"SKILL.md", "README.md", "CHANGELOG.md", "manifest.json", "agents", "references", "assets", "evals", "scripts"}
IGNORED_NAMES = {"manifest.json"}
FORBIDDEN_PARTS = {"__pycache__", ".pytest_cache", ".DS_Store", "Thumbs.db"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect(skill_dir: Path) -> list[Path]:
    unknown = sorted(p.name for p in skill_dir.iterdir() if p.name not in ALLOWED_TOP)
    if unknown:
        raise ValueError(f"Unknown top-level entries: {', '.join(unknown)}")
    files: list[Path] = []
    for path in sorted(skill_dir.rglob("*"), key=lambda p: p.as_posix()):
        if path.is_symlink():
            raise ValueError(f"Symlinks are not allowed: {path}")
        if not path.is_file() or path.name in IGNORED_NAMES:
            continue
        rel = path.relative_to(skill_dir)
        if any(part in FORBIDDEN_PARTS or part.endswith((".tmp", ".bak")) for part in rel.parts):
            raise ValueError(f"Temporary/cache file is not allowed: {rel.as_posix()}")
        files.append(path)
    required = {"SKILL.md", "README.md", "CHANGELOG.md", "agents/openai.yaml"}
    present = {p.relative_to(skill_dir).as_posix() for p in files}
    missing = required - present
    if missing:
        raise ValueError(f"Missing required release files: {', '.join(sorted(missing))}")
    return files


def write_manifest(skill_dir: Path, files: list[Path]) -> Path:
    entries = [
        {
            "path": path.relative_to(skill_dir).as_posix(),
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
        for path in files
    ]
    manifest = {
        "name": NAME,
        "version": VERSION,
        "schema_version": 1,
        "file_count": len(entries),
        "files": entries,
    }
    target = skill_dir / "manifest.json"
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target


def build(skill_dir: Path, output_dir: Path) -> tuple[Path, Path]:
    if skill_dir.resolve().name != NAME:
        raise ValueError(f"Skill directory must be named {NAME}")
    files = collect(skill_dir)
    manifest = write_manifest(skill_dir, files)
    release_files = collect(skill_dir) + [manifest]
    release_files = sorted(set(release_files), key=lambda p: p.relative_to(skill_dir).as_posix())

    output_dir.mkdir(parents=True, exist_ok=True)
    standalone = output_dir / f"{NAME}-v{VERSION}-SKILL.md"
    shutil.copyfile(skill_dir / "SKILL.md", standalone)

    zip_target = output_dir / f"{NAME}-v{VERSION}.zip"
    fd, temp_name = tempfile.mkstemp(prefix=f".{NAME}-", suffix=".zip", dir=output_dir)
    os.close(fd)
    temp_zip = Path(temp_name)
    try:
        with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in release_files:
                rel = path.relative_to(skill_dir).as_posix()
                info = zipfile.ZipInfo(f"{NAME}/{rel}", date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                mode = 0o100755 if rel.startswith("scripts/") and path.suffix in {".sh", ".py"} else 0o100644
                info.external_attr = mode << 16
                archive.writestr(info, path.read_bytes())
        os.replace(temp_zip, zip_target)
    finally:
        if temp_zip.exists():
            temp_zip.unlink()
    return zip_target, standalone


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    try:
        zip_path, standalone = build(args.skill_dir.resolve(), args.output_dir.resolve())
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        return 1
    print(f"Built {zip_path}")
    print(f"Built {standalone}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
