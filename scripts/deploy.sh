#!/bin/bash

# Stop any running Flask app
pkill -f "flask run"

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask app with Gunicorn
gunicorn --workers 4 --bind 0.0.0.0:5000 app.main:app &

echo "App deployed and running on http://0.0.0.0:5000"
