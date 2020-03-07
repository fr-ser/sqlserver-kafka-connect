#!/bin/bash

set -e

docker-compose build
docker-compose up -d sqlserver postgres
docker-compose run kafka-cli
docker-compose up -d kafka-connect
docker-compose run sqlserver-cli
docker-compose up -d faust
docker-compose run debezium
