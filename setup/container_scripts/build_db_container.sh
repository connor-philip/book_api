#!/bin/bash

CONTAINER_SCRIPTS_DIR="${0%/*}"
SETUP_DIR=$CONTAINER_SCRIPTS_DIR/..
BOOK_API_DIR=$SETUP_DIR/..
MONGO_CONTAINER_IP=$(grep mongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

cd $BOOK_API_DIR

docker build --tag book_api_db_server -f setup/db_container/db.Dockerfile . && \
docker run --net booknet --ip $MONGO_CONTAINER_IP --name book_api_db -d book_api_db_server

cd -
