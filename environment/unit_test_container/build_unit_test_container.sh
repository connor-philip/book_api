#!/bin/bash

UNIT_TEST_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$UNIT_TEST_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
TEST_MONGO_CONTAINER_IP=$(awk '/testMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)

cd $BOOK_API_DIR

docker build --build-arg databaseIP=$TEST_MONGO_CONTAINER_IP --tag book_api_unit_tests --file environment/unit_test_container/unit_test.Dockerfile .

cd -