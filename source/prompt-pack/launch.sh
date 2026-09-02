#!/usr/bin/env bash
# Launches the four AI Friday design sessions in Claude Code.
# Usage: ./launch.sh            -> tmux session "aifriday" with one window per direction
#        ./launch.sh --critic   -> same, but starts each session on CRITIC.md
set -e
cd "$(dirname "$0")"
DIRS=(01-shotgun-house 02-front-porch 03-shop-sign 04-combined)
FILE=PROMPT.md; [[ "$1" == "--critic" ]] && FILE=CRITIC.md

# share reference images
for d in "${DIRS[@]}"; do cp -n refs/* "$d/refs/" 2>/dev/null || true; done

command -v claude >/dev/null || { echo "claude CLI not found. Install: npm i -g @anthropic-ai/claude-code"; exit 1; }
command -v codex  >/dev/null || echo "warning: codex CLI not found; image generation will fail."

if command -v tmux >/dev/null; then
  tmux kill-session -t aifriday 2>/dev/null || true
  tmux new-session -d -s aifriday -n "${DIRS[0]}" -c "$PWD/${DIRS[0]}" "claude \"\$(cat $FILE)\""
  for d in "${DIRS[@]:1}"; do
    tmux new-window -t aifriday -n "$d" -c "$PWD/$d" "claude \"\$(cat $FILE)\""
  done
  echo "Launched. Attach with:  tmux attach -t aifriday   (Ctrl-b n / Ctrl-b p to switch windows)"
else
  echo "tmux not found. Open four terminals and run in each directory:"
  for d in "${DIRS[@]}"; do echo "  cd $PWD/$d && claude \"\$(cat $FILE)\""; done
fi
