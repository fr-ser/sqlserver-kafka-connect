#!/bin/bash

set -e

docker-compose build
docker-compose up -d mssql postgres
docker-compose run kafka-cli
docker-compose run mssql-tools
docker-compose up -d faust
docker-compose run debezium
