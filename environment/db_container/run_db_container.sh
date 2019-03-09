#!/bin/bash

environment=$1

DB_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$DB_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
DEV_MONGO_CONTAINER_IP=$(awk '/devMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
UNIT_TEST_MONGO_CONTAINER_IP=$(awk '/unitTestMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)

cd $BOOK_API_DIR

if [[ $environment == "unit_test" ]]; then
    docker run --net booknet --ip $UNIT_TEST_MONGO_CONTAINER_IP --name book_api_unit_tests_db --detach book_api_db_server
else
    docker run --net booknet --ip $DEV_MONGO_CONTAINER_IP --name book_api_db --detach book_api_db_server
fi

cd -
