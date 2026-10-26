#!/usr/bin/env sh
set -eu

skill_name="vibe-product-director"
script_dir="$(cd "$(dirname "$0")" && pwd -P)"
source_dir="$(cd "$script_dir/.." && pwd -P)"
target_root="${HOME}/.agents/skills"
dry_run=0
force=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target) [ "$#" -ge 2 ] || { echo "--target needs a path" >&2; exit 2; }; target_root="$2"; shift 2 ;;
    --dry-run) dry_run=1; shift ;;
    --force) force=1; shift ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done

mkdir -p "$target_root"
target_root="$(cd "$target_root" && pwd -P)"
home_full="$(cd "$HOME" && pwd -P)"
[ "$target_root" != "/" ] && [ "$target_root" != "$home_full" ] || { echo "Unsafe target root: $target_root" >&2; exit 1; }
target_dir="$target_root/$skill_name"
stamp="$(date +%Y%m%d-%H%M%S)"
backup_dir="$target_dir.backup-$stamp"
stage_dir="$target_root/.$skill_name.stage-$$"

validate_package() {
  [ -f "$1/SKILL.md" ] && [ -f "$1/manifest.json" ] &&
    grep -Eq '"name"[[:space:]]*:[[:space:]]*"vibe-product-director"' "$1/manifest.json" &&
    grep -Eq '"version"[[:space:]]*:[[:space:]]*"2\.0\.0"' "$1/manifest.json"
}

validate_package "$source_dir" || { echo "Source package is not built or valid: $source_dir" >&2; exit 1; }
if [ "$dry_run" -eq 1 ]; then
  echo "DRY RUN: install $source_dir to $target_dir"
  [ ! -e "$target_dir" ] || echo "Existing target: overwrite requires --force and creates $backup_dir"
  exit 0
fi

if [ -e "$target_dir" ]; then
  if [ -f "$target_dir/manifest.json" ] && cmp -s "$source_dir/manifest.json" "$target_dir/manifest.json"; then
    echo "Already installed: $target_dir"
    exit 0
  fi
  [ "$force" -eq 1 ] || { echo "A different installation exists at $target_dir. Re-run with --force." >&2; exit 1; }
fi

moved_old=0
restore_on_error() {
  status=$?
  if [ "$status" -ne 0 ]; then
    [ ! -e "$stage_dir" ] || mv "$stage_dir" "$stage_dir.failed"
    if [ "$moved_old" -eq 1 ] && [ ! -e "$target_dir" ] && [ -e "$backup_dir" ]; then mv "$backup_dir" "$target_dir"; fi
  fi
  exit $status
}
trap restore_on_error EXIT
cp -R "$source_dir" "$stage_dir"
validate_package "$stage_dir"
if [ -e "$target_dir" ]; then mv "$target_dir" "$backup_dir"; moved_old=1; fi
mv "$stage_dir" "$target_dir"
trap - EXIT
echo "Installed to $target_dir"
[ "$moved_old" -eq 0 ] || echo "Previous installation backed up to $backup_dir"
