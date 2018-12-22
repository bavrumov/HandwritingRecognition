#!/usr/bin/env bash


if [ `ls input.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
    echo hi
    for file in input.jpg; do
        convert -flatten input.jpg input.jpg
        convert "$file" -resize 28x28\! "scaledinput.jpg"
        file "$file"
    done
fi


if [ `ls input.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
    echo hi
    for file in input.jpg; do
        convert -flatten input.jpg input.jpg
        convert "$file" -resize 28x28\! "scaledinput.jpg"
        file "$file"
        rm "$file"
    done
fi