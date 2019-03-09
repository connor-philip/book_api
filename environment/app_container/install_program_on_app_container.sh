#!/bin/bash

# NOTE: The app is already installed on docker build
# This just provides a way to reinstall without having to rebuilding the container

APP_CONTAINER_DIR="${0%/*}"
ENVIRONMENT_DIR=$APP_CONTAINER_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..

cd $BOOK_API_DIR

docker exec book_api_app rm -rf /var/www/book_api/program
docker cp program book_api_app:/var/www/book_api/program
docker exec book_api_app pip3 install /var/www/book_api/ --upgrade
docker exec book_api_app service apache2 reload

cd -