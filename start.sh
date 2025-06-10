#!/bin/bash
# Startup script for Render deployment

echo "Starting portfolio application..."
echo "Python version: $(python --version)"
echo "Current directory: $(pwd)"
echo "Files in directory: $(ls -la)"

# Check if wsgi.py exists
if [ -f "wsgi.py" ]; then
    echo "Found wsgi.py, starting with Gunicorn..."
    exec gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
else
    echo "ERROR: wsgi.py not found!"
    exit 1
fi
