#!/bin/bash

DB_CONTAINER_DIR="${0%/*}"
SETUP_DIR=$DB_CONTAINER_DIR/..
BOOK_API_DIR=$SETUP_DIR/..

cd $BOOK_API_DIR

docker build --tag book_api_db_server -f setup/db_container/db.Dockerfile .

cd -
