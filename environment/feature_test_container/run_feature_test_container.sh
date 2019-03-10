#!/bin/bash

FEATURE_TEST_CONTAINER_dir="${0%/*}"
ENVIRONMENT_DIR=$FEATURE_TEST_CONTAINER_dir/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..


cd $BOOK_API_DIR
ABSOLUTE_BOOK_API_DIR=$(pwd)
FEATURE_TEST_DIR=$ABSOLUTE_BOOK_API_DIR/tests/feature_tests
ls $FEATURE_TEST_DIR

docker run --net booknet --label book_api_feature_tests_container --volume $FEATURE_TEST_DIR/:/app/book_api/tests/feature_tests book_api_feature_tests

cd -