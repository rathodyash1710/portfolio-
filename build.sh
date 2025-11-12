#!/usr/bin/env bash
# Exit on error
set -o errexit

# Step 1: Install Python packages
pip install -r requirements.txt

# Step 2: Collect static files (CSS, JS, images)
python manage.py collectstatic --no-input

# Step 3: Apply database migrations
python manage.py migrate
