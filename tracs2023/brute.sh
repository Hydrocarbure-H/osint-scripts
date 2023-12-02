#!/bin/bash

while true; do
    echo "Restarting script..."
    timeout 60s python3 brute-multi.py
    if [ $? -eq 0 ]; then
        break
    fi
done
