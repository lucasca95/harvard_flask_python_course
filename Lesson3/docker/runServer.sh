#!/bin/bash

docker-compose down

docker rm -f -v control
docker rm -f -v db_postgres
docker volume rm -f postgres_db_vol

docker-compose up