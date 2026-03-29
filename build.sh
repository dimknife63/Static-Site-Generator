#!/bin/bash

# Delete old docs
echo "Deleting docs directory..."
rm -rf docs

# Copy static files
echo "Copying static files to docs directory..."
mkdir -p docs
cp -r static docs/

# Generate HTML content
echo "Generating content..."
python3 src/gencontent.py