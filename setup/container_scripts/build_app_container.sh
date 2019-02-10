#!/bin/bash

CONTAINER_SCRIPTS_DIR="${0%/*}"
SETUP_DIR=$CONTAINER_SCRIPTS_DIR/..
BOOK_API_DIR=$SETUP_DIR/..
MONGO_CONTAINER_IP=$(grep mongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

cd $BOOK_API_DIR

docker build --build-arg databaseIP=$MONGO_CONTAINER_IP --tag book_api_app_server -f setup/app_container/app.Dockerfile . && \
docker run --network=host  --name book_api_app -d -P book_api_app_server

cd -