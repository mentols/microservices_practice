#!/bin/bash

# Load environment variables from .env file
source .env

set -e
export PYTHONPATH=/core/:$PYTHONPATH
#alembic upgrade head && while !</dev/tcp/db/5432; do sleep 1; done; uvicorn app.main:app --host 0.0.0.0 --reload --port 8000
#pytest app/tests
uvicorn app.main:app --host 0.0.0.0 --reload --port 8000