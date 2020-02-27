#!/bin/bash

docker-compose run kafka-cli
docker-compose run mssql-tools
docker-compose up -d