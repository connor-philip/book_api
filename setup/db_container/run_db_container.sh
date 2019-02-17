#!/bin/bash

DB_CONTAINER_DIR="${0%/*}"
SETUP_DIR=$DB_CONTAINER_DIR/..
BOOK_API_DIR=$SETUP_DIR/..
MONGO_CONTAINER_IP=$(grep mongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

cd $BOOK_API_DIR

docker run --net booknet --ip $MONGO_CONTAINER_IP --name book_api_db -d book_api_db_server

cd -
