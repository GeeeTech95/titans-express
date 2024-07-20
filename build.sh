#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate


#!/bin/bash

# Define the version of wkhtmltopdf you want to download
WKHTMLTOPDF_VERSION=0.12.6

# Create a directory for wkhtmltopdf
mkdir -p ~/wkhtmltopdf

# Download the precompiled binary
wget https://github.com/wkhtmltopdf/packaging/releases/download/${WKHTMLTOPDF_VERSION}-1/wkhtmltox_${WKHTMLTOPDF_VERSION}-1.bionic_amd64.deb -P ~/wkhtmltopdf

# Extract the contents of the .deb package
dpkg-deb -x ~/wkhtmltopdf/wkhtmltox_${WKHTMLTOPDF_VERSION}-1.bionic_amd64.deb ~/wkhtmltopdf

# Set the WKHTMLTOPDF_CMD environment variable to the path of the binary
export WKHTMLTOPDF_CMD=~/wkhtmltopdf/usr/local/bin/wkhtmltopdf

# Add the binary path to your PATH
export PATH=$PATH:~/wkhtmltopdf/usr/local/bin

# Verify the installation
wkhtmltopdf --version


