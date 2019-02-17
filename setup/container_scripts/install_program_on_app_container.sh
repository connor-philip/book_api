#!/bin/bash

# NOTE: The app is already installed on docker build
# This just provides a way to reinstall without rebuilding the container

CONTAINER_SCRIPTS_DIR="${0%/*}"
SETUP_DIR=$CONTAINER_SCRIPTS_DIR/..
BOOK_API_DIR=$SETUP_DIR/..

cd $BOOK_API_DIR

docker exec book_api_app rm -rf /var/www/book_api/program
docker cp program book_api_app:/var/www/book_api/program
docker exec book_api_app pip3 install /var/www/book_api/ --upgrade
docker exec book_api_app service apache2 reload

cd -