#!/bin/bash

APP_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$APP_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..

cd $BOOK_API_DIR

docker run --network=host  --name book_api_app -d -P book_api_app_server

cd -