#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn frontend.wsgi:application \
    --bind 0.0.0.0:8001 \
    --workers 3
