#!/bin/bash

# Load environment variables from .env file
#source .env

set -e
export PYTHONPATH=/core/:$PYTHONPATH


if [[ "$1" == "fastapi" ]]; then
  uvicorn app.main:app --host 0.0.0.0 --reload --port 8009
  echo "FastAPI server successful startup"
elif [[ "$1" == "consumer" ]]; then
  exec python app/consumer.py
  echo "Consumer successful startup"
else
  exec "$@"
fi