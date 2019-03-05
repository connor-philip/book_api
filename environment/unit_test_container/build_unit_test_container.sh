#!/bin/bash

UNIT_TEST_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$UNIT_TEST_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
UNIT_TEST_MONGO_CONTAINER_IP=$(grep unitTestMongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

cd $BOOK_API_DIR

docker build --build-arg databaseIP=$UNIT_TEST_MONGO_CONTAINER_IP --tag book_api_unit_tests --file environment/unit_test_container/unit_test.Dockerfile .

cd -