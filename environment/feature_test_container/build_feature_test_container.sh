#!/bin/bash

FEATURE_TEST_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$FEATURE_TEST_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
TEST_APP_CONTAINER_IP=$(awk '/testAppContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
TEST_MONGO_CONTAINER_IP=$(awk '/testMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)

cd $BOOK_API_DIR

docker build --build-arg testServerIP=$TEST_APP_CONTAINER_IP --build-arg testDatabaseIP=$TEST_MONGO_CONTAINER_IP --tag book_api_feature_tests --file environment/feature_test_container/feature_test.Dockerfile .

cd -