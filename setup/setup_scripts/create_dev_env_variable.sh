#!/bin/bash

SETUP_SCRIPTS_DIR="${0%/*}"
SETUP_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$SETUP_DIR/..
MONGO_CONTAINER_IP=$(grep devMongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

echo "databaseIP=$MONGO_CONTAINER_IP" >> /etc/environment
