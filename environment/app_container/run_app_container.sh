#!/bin/bash

environment=$1

APP_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$APP_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..

DEV_APP_CONTAINER_IP=$(awk '/devAppContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
TEST_APP_CONTAINER_IP=$(awk '/testAppContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
TEST_MONGO_CONTAINER_IP=$(awk '/testMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)

cd $BOOK_API_DIR

if [[ $environment == "test" ]]; then
    docker run --net booknet --ip $TEST_APP_CONTAINER_IP --publish 8080:80  --env databaseIP=$TEST_MONGO_CONTAINER_IP --name book_api_test_app --detach book_api_app_server
else
    docker run --net booknet --ip $DEV_APP_CONTAINER_IP --publish 80:80 --name book_api_app --detach book_api_app_server
fi

cd -