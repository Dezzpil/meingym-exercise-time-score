#!/bin/bash

# Stop any running Flask app
pkill -f "flask run"

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask app with Gunicorn
gunicorn --workers 2 --bind 127.0.0.1:5001 app.main:app &
echo "App deployed and running on http://127.0.0.1:5001"
