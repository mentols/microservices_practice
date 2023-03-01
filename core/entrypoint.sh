#!/bin/bash

# Load environment variables from .env file
source .env

set -e
export PYTHONPATH=/core/:$PYTHONPATH
uvicorn app.main:app --host ${FASTAPI_HOST} --reload --port ${FASTAPI_PORT}