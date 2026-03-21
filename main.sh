#!/bin/bash
python3 src/main.py        # generate the public/index.html
cd public && python3 -m http.server 8888