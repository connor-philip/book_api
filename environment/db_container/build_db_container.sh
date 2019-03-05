#!/bin/bash

DB_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$DB_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..

cd $BOOK_API_DIR

docker build --tag book_api_db_server --file environment/db_container/db.Dockerfile .

cd -
