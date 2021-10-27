#!/usr/bin/env bash
if [[ -d "/media/CIRCUITPY" ]]; then
    echo "Copying"
    cp *.py /media/CIRCUITPY
    cp -r beepad /media/CIRCUITPY
    # cp -r lib /media/CIRCUITPY
fi