#!/bin/bash

set -e

if [ "$1" == "--bootstrap" ]; then
    ./bootstrap.sh
fi

PYTHONPATH=./src pipenv run pytest tests
