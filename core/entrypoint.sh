#!/bin/bash

# Load environment variables from .env file
source .env

set -e
export PYTHONPATH=/core/:$PYTHONPATH
uvicorn app.main:app --host 0.0.0.0 --reload --port 8000