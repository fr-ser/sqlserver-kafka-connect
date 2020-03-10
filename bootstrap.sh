#!/bin/bash

set -e

if [ "${SLIM}" == "true" ]; then
    DOCKER_COMPOSE_FILE="docker-compose.slim.yaml"
else
    DOCKER_COMPOSE_FILE="docker-compose.yaml"
fi

docker-compose --file ${DOCKER_COMPOSE_FILE} build
docker-compose --file ${DOCKER_COMPOSE_FILE} up -d sqlserver postgres
docker-compose --file ${DOCKER_COMPOSE_FILE} run kafka-cli
docker-compose --file ${DOCKER_COMPOSE_FILE} up -d kafka-connect
docker-compose --file ${DOCKER_COMPOSE_FILE} run sqlserver-cli
docker-compose --file ${DOCKER_COMPOSE_FILE} up -d faust
docker-compose --file ${DOCKER_COMPOSE_FILE} run debezium
