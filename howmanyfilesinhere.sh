#!/bin/bash

set -euo pipefail

count_files() {
    find "$1" -type f -print0 | LC_ALL=C tr -cd '\000' | wc -c
}

total=$(count_files .)
printf 'Regular files in %s: %d\n' "$PWD" "$total"
printf 'Files in each immediate folder (including hidden folders):\n'
find . -mindepth 1 -maxdepth 1 -type d -print0 |
    while IFS= read -r -d '' directory; do
        count=$(count_files "$directory")
        printf '  %q: %d\n' "$directory" "$count"
    done
