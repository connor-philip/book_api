#!/bin/bash

SETUP_SCRIPTS_DIR="${0%/*}"
ENVIRONMENT_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
MONGO_CONTAINER_IP=$(grep devMongoContainerIp $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')
LOG_PATH=$(grep bookApilogPath $BOOK_API_DIR/config.py | grep -Po '((?:\/\w+)+\/?)')

echo "databaseIP=$MONGO_CONTAINER_IP" >> /etc/environment
echo "book_api_logs=$LOG_PATH" >> /etc/environment
