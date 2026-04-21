#!/bin/bash

######################################################################
# Bespoke script to edit files in https://ncas-cms.github.io/canari/ #
######################################################################

PERIOD="ssp370" # or "hist2"

# 1. Load Conda environment settings
source ~/.bashrc

# 2. Define the path to ID file
ID_FILE="$HOME/canari/docs/${PERIOD}/runids"

# 3. Loop through the file
# 'read' takes the first column as 'member' and the second as 'runid'
while read -r member runid; do

    # Skip the header line or any other lines starting with '#'
    [[ "$member" =~ ^#.*$ ]] && continue
    # Skip empty lines
    [[ -z "$member" ]] && continue

    # Construct variables
    # ${runid:2} removes the 'u-' prefix for the filename
    short_id="${runid:2}"
    filename="/home/users/jonnyhtw/canari/docs/${PERIOD}/${member}-${short_id}.md"
    
    # Define the core JDMA command
    jdma_cmd="jdma batch -f workspace -w canari | grep ${runid} | grep -viE \"deleted|failed\" | cat -n"

    # --- Processing Member ${member} (ID: ${runid}) ---
    echo "Generating ${filename}..."

    # Create the file with opening backticks
    echo '```' >> "$filename"
    
    # Add a label showing which command was run
    echo "$ ${jdma_cmd}" >> "$filename"
    
    # Execute the command and append the output
    # 'eval' ensures the pipes (|) in the variable are processed correctly
    eval "$jdma_cmd" >> "$filename"
    
    # Add closing backticks
    echo '```' >> "$filename"

done < "$ID_FILE"

echo "Done! Check docs/${PERIOD}/ for results."
