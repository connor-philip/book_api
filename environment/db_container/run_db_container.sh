#!/bin/bash

environment=$1

DB_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$DB_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
DEV_MONGO_CONTAINER_IP=$(grep devMongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')
UNIT_TEST_MONGO_CONTAINER_IP=$(grep unitTestMongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

cd $BOOK_API_DIR

if [[ $environment == "unit_test" ]]; then
    docker run --net booknet --ip $UNIT_TEST_MONGO_CONTAINER_IP --name book_api_unit_tests_db -d book_api_db_server
else
    docker run --net booknet --ip $DEV_MONGO_CONTAINER_IP --name book_api_db -d book_api_db_server
fi

cd -
