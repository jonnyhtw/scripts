#!/bin/bash

# Capture current directory before changing path
EXEC_DIR="$(pwd)"
LOGFILE="${EXEC_DIR}/_full_transfer.log"
LISTFILE="${EXEC_DIR}/_symlink_list.txt"

# Configuration
SOURCE_DIR="/work/y07/shared/umshared/"
DEST_SERVER="umshared@sci-vm-01.jasmin.ac.uk"
DEST_DIR="/gws/ssde/j25b/umshared/umshared/"

# Set DRY_RUN=true to test safety before actual transfer
DRY_RUN=false

# Change to source directory
cd "$SOURCE_DIR" || { echo "Failed to change directory to $SOURCE_DIR"; exit 1; }

echo "Finding all symbolic links..."
# Use find to locate only symlinks (-type l) and store relative paths
find . -type l > "$LISTFILE"

# Main rsync flags:
# -l preserves symlinks as symlinks
# -r creates destination parent directory structures
# -t preserves timestamps
# -v lists every symlink being copied
FLAGS="-lrtv --stats --files-from=$LISTFILE"

if [ "$DRY_RUN" = true ]; then
  FLAGS="$FLAGS --dry-run"
fi

CMD="rsync $FLAGS . ${DEST_SERVER}:${DEST_DIR}"

# Write Log Header
{
  echo "=== Symlink-Only Transfer Started: $(date) ==="
  echo "Source Directory: $(pwd)"
  echo "Symlinks found: $(wc -l < "$LISTFILE")"
  echo "Command Executed: $CMD"
  echo "--------------------------------------------------------------------------------"
} > "$LOGFILE"

START_TIME=$(date +%s)

# Execute pipeline and capture all output
( eval "$CMD" ) 2>&1 | tee -a "$LOGFILE"

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

# Clean up temporary list file
rm -f "$LISTFILE"

# Write Log Footer
{
  echo -e "\n--------------------------------------------------------------------------------"
  echo "=== Transfer Completed: $(date) ==="
  echo "Total duration: ${ELAPSED} seconds"
} >> "$LOGFILE"
