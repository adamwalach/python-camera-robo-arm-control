#!/bin/bash

mount -t tmpfs -o size=10M tmpfs ./output/images 

echo "Start"
python web.py &

echo "Web server started"
while true
do
    echo "Face recognition start"
    python -u face.py
done
