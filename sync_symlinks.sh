#!/bin/bash

# Configuration
SOURCE_DIR="/work/y07/shared/umshared"
DEST_SERVER="umshared@sci-vm-01.jasmin.ac.uk"
DEST_DIR="/gws/ssde/j25b/umshared/umshared/"
LOGFILE="$HOME/symlink_transfer.log"

# Define the rsync command
# Set DRY_RUN=true to test without transferring files
DRY_RUN=false

FLAGS="-av --stats"
if [ "$DRY_RUN" = true ]; then
  FLAGS="$FLAGS --dry-run"
fi

CMD="find . -type l \( -xtype f -o -xtype d \) | rsync $FLAGS --files-from=- ./ ${DEST_SERVER}:${DEST_DIR}"

# Change to working directory
cd "$SOURCE_DIR" || { echo "Failed to change directory to $SOURCE_DIR"; exit 1; }

# Write Log Header
{
  echo "=== Transfer Started: $(date) ==="
  echo "Working Directory: $(pwd)"
  echo "Command Executed: $CMD"
  echo "Note: Directory names listed indicate metadata checks/path traversal, NOT file copies."
  echo "--------------------------------------------------------------------------------"
} > "$LOGFILE"

START_TIME=$(date +%s)

# Execute pipeline and capture all output
( eval "$CMD" ) 2>&1 | tee -a "$LOGFILE"

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

# Write Log Footer
{
  echo -e "\n--------------------------------------------------------------------------------"
  echo "=== Transfer Completed: $(date) ==="
  echo "Total duration: ${ELAPSED} seconds"
} >> "$LOGFILE"
