#!/bin/bash
# ===============================================================================
# CMIP7 REPACK SLURM WORKER SCRIPT (SEQUENTIAL LOOP VERSION)
# ===============================================================================
# How to run:
# (1) split -l 250 -d -a 5 --additional-suffix=.txt all_files.txt manifest_chunk_
# (2) for CHUNK in manifest_chunk_*.txt; do
#         sbatch -J "cmip7repack_${CHUNK%.txt}" ~/scripts/submit_repack.sh "$CHUNK"
#         echo "Submitted $CHUNK"
#     done
# (3) Verification:
#     for f in $(shuf -n 10 all_files.txt); do echo "$f"; check_cmip7_packing "$f"; done

#SBATCH --job-name=cmip7repack
#SBATCH --output=/home/users/jonnyhtw/%x_%j.out
#SBATCH --error=/home/users/jonnyhtw/%x_%j.err
#SBATCH --export=ALL
#SBATCH --account=canari
#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --time=24:00:00
#SBATCH --mem=128G

MANIFEST_FILE="$1"

if [ -z "$MANIFEST_FILE" ] || [ ! -f "$MANIFEST_FILE" ]; then
    echo "Error: Manifest file '$MANIFEST_FILE' not found."
    exit 1
fi

# Loop through every line in the chunk sequentially
while IFS= read -r TARGET_FILE || [ -n "$TARGET_FILE" ]; do
    if [ -f "$TARGET_FILE" ]; then
        # Only repack if check_cmip7_packing returns non-zero (fails validation)
        if ! check_cmip7_packing "$TARGET_FILE" > /dev/null 2>&1; then
            echo "PACKING FAIL: Repacking $TARGET_FILE..."
            cmip7repack -o "$TARGET_FILE" && echo "COMPLETED: $TARGET_FILE"
        else
            echo "SKIPPED (Packing OK): $TARGET_FILE"
        fi
    else
        echo "WARNING: File not found: $TARGET_FILE"
    fi
done < "$MANIFEST_FILE"
