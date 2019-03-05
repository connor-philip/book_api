#!/bin/bash

APP_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$APP_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
MONGO_CONTAINER_IP=$(grep devMongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

cd $BOOK_API_DIR

docker build --build-arg databaseIP=$MONGO_CONTAINER_IP --tag book_api_app_server -f environment/app_container/app.Dockerfile .

cd -