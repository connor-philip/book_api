#!/bin/bash

SETUP_SCRIPTS_DIR="${0%/*}"
ENVIRONMENT_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
MONGO_CONTAINER_IP=$(awk '/devMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
LOG_PATH=$(awk '/bookApilogPath/ {print $2}' $BOOK_API_DIR/build_config.txt)

echo "databaseIP=$MONGO_CONTAINER_IP" >> /etc/environment
echo "book_api_logs=$LOG_PATH" >> /etc/environment
