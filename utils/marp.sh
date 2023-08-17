#!/bin/bash
rm commands_marp_auto.txt
for file in new_output/*/slide.md; do
    
    # echo $file
    # npx @marp-team/marp-cli "$file" --html --images png --allow-local-files --theme-set ./themes
    # npx @marp-team/marp-cli "$file" --html --allow-local-files --theme-set ./themes
    echo "npx @marp-team/marp-cli \"$file\" --html --images jpeg --allow-local-files --theme-set ./themes" >> commands_marp_auto.txt
    echo "npx @marp-team/marp-cli \"$file\" --html --allow-local-files --theme-set ./themes" >> commands_marp_auto.txt
    
done