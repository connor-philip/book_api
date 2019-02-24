#!/bin/bash

APP_CONTAINER_DIR="${0%/*}"
SETUP_DIR=$APP_CONTAINER_DIR/..
BOOK_API_DIR=$SETUP_DIR/..

cd $BOOK_API_DIR

docker run --network=host  --name book_api_app -d -P book_api_app_server

cd -