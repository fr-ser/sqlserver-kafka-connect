#!/bin/bash

set -e


if [ "${BOOTSTRAP}" == "true" ]; then
    ./bootstrap.sh
fi

PYTHONPATH=./src pipenv run pytest tests
