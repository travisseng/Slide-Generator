#!/bin/bash
rm commands_locator_auto.txt
for file in new_output/*/slide.html; do
    
    # echo $file
    directory=$(dirname "$file")
    # echo "locator --output \"$directory\"/images --force --input \"$file\"" >> commands.txt
    echo "locator --input \"$file\" > \"$directory/boxes.json\"" >> commands_locator_auto.txt
done