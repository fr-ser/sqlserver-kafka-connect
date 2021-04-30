#!/bin/bash

set -e

: ${SLEEP_LENGTH:=2}
: ${TIMEOUT_LENGTH:=60}

START=$(date +%s)
while ! curl --fail --silent --output /dev/null localhost:8083/connector-plugins; do
    if [ $(($(date +%s) - $START)) -gt $TIMEOUT_LENGTH ]; then
        echo "KafkaConnect did not start within $TIMEOUT_LENGTH seconds. Aborting..."
        exit 1
    fi
    echo "waiting for KafkaConnect to start"
    sleep $SLEEP_LENGTH
done
