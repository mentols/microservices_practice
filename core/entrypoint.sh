#!/bin/bash

set -e
export PYTHONPATH=/core/:$PYTHONPATH
uvicorn app.main:app --host 0.0.0.0 --reload --port 8000