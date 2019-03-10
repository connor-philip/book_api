#!/bin/bash

UNIT_TEST_CONTAINER_dir="${0%/*}"
ENVIRONMENT_DIR=$UNIT_TEST_CONTAINER_dir/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..

cd $BOOK_API_DIR
ABSOLUTE_BOOK_API_DIR=$(pwd)


docker run --net booknet --label book_api_unit_tests_container --volume $ABSOLUTE_BOOK_API_DIR/:/app book_api_unit_tests

cd -