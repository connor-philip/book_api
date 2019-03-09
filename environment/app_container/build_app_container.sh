#!/bin/bash

APP_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$APP_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
MONGO_CONTAINER_IP=$(awk '/devMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)

cd $BOOK_API_DIR

docker build --build-arg databaseIP=$MONGO_CONTAINER_IP --tag book_api_app_server --file environment/app_container/app.Dockerfile .

cd -