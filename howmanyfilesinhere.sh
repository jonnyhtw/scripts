#!/bin/bash

echo 'there are this many files in...'
echo "$PWD"
find . -true -print | wc -l


echo 'and this is how they are distributed across folders (including hidden ones)...'
find . -maxdepth 1 -mindepth 1 -type d -print0 | xargs -0 -I {} sh -c 'echo -n "{}      " && { find {} -true -print | wc -l ; }'
