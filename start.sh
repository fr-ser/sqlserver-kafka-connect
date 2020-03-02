#!/bin/bash

set -e

docker-compose build
docker-compose up -d mssql
docker-compose run kafka-cli
docker-compose run mssql-tools
docker-compose run debezium
