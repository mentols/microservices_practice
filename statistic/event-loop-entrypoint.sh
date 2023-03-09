#!/bin/bash

set -e
export PYTHONPATH=/microservice/:$PYTHONPATH

exec python app/consumer.py
