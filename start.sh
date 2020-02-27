#!/bin/bash

docker-compose up -d mssql
docker-compose run kafka-cli
docker-compose run mssql-tools
docker-compose up -d
docker-compose logs -f kafka-connect
