#!/usr/bin/env bash
# ABOUTME: Copies the four sprint builds from the working sprint folder into designs/,
# ABOUTME: leaving out raw generation sources and tooling, and converts screenshots to WebP.
set -euo pipefail
cd "$(dirname "$0")/.."

SRC="${1:-$HOME/dev/aifri-design/ai-friday-redesign}"
DIRS=(01-shotgun-house 02-front-porch 03-shop-sign 04-combined)

command -v rsync >/dev/null || { echo "rsync not found"; exit 1; }
command -v magick >/dev/null || { echo "magick not found (brew install imagemagick)"; exit 1; }

for d in "${DIRS[@]}"; do
  [ -d "$SRC/$d" ] || { echo "skip $d: not in $SRC"; continue; }
  mkdir -p "designs/$d/screenshots"
  rsync -a --delete \
    --exclude '.DS_Store' --exclude '.gitignore' --exclude '.seed' \
    --exclude '.playwright-mcp/' --exclude 'node_modules/' \
    --exclude 'assets/src/' --exclude 'assets/_src/' --exclude 'assets/*.tmp' \
    --exclude 'tools/' --exclude 'refs/' --exclude 'screenshots/' \
    --exclude '/v*.png' --exclude '/notes.html' \
    "$SRC/$d/" "designs/$d/"
  # Screenshots: PNG -> WebP, capped at 1600px wide and 16000px tall (WebP limit).
  find "designs/$d/screenshots" -name '*.webp' -delete
  shopt -s nullglob
  for png in "$SRC/$d/screenshots"/*.png; do
    out="designs/$d/screenshots/$(basename "${png%.png}").webp"
    magick "$png" -resize '1600x16000>' -quality 80 "$out"
  done
  shopt -u nullglob
  echo "synced $d ($(du -sh "designs/$d" | cut -f1))"
done

# The shared pack that sat above the four folders.
mkdir -p source/prompt-pack
cp "$SRC/README.md" "$SRC/POLISH.md" "$SRC/launch.sh" source/prompt-pack/
echo "synced source/prompt-pack"
