#!/bin/bash
# ===============================================================================
# CMIP7 REPACK SLURM WORKER SCRIPT (SEQUENTIAL LOOP VERSION)
# ===============================================================================
# How to run:
# (1) split -l 1000 -d -a 3 --additional-suffix=.txt all_files.txt manifest_chunk_
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
#SBATCH --qos=short
#SBATCH --time=04:00:00
#SBATCH --mem=150G

MANIFEST_FILE="$1"

if [ -z "$MANIFEST_FILE" ] || [ ! -f "$MANIFEST_FILE" ]; then
    echo "Error: Manifest file '$MANIFEST_FILE' not found."
    exit 1
fi

# Loop through every line in the chunk sequentially
while IFS= read -r TARGET_FILE || [ -n "$TARGET_FILE" ]; do
    if [ -f "$TARGET_FILE" ]; then
        cmip7repack -o "$TARGET_FILE" && echo "COMPLETED: $TARGET_FILE"
    fi
done < "$MANIFEST_FILE"
