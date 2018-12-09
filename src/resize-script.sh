#!/usr/bin/env bash


if [ `ls data/input.png 2> /dev/null | wc -l ` -gt 0 ]; then
    echo hi
    for file in data/input.png; do
        convert "$file" -resize 28x28\! "scaledinput.png"
        file "$file"
    done
fi


if [ `ls data/input.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
    echo hi
    for file in data/input.jpg; do
        convert "$file" -resize 28x28\! "scaledinput.png"
        file "$file"
        rm "$file"
    done
fi