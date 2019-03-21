#!/bin/bash

SETUP_SCRIPTS_DIR="${0%/*}"
ENVIRONMENT_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
TEST_APP_CONTAINER_IP=$(awk '/testAppContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
TEST_MONGO_CONTAINER_IP=$(awk '/testMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
MONGO_CONTAINER_IP=$(awk '/devMongoContainerIp/ {print $2}' $BOOK_API_DIR/build_config.txt)
LOG_PATH=$(awk '/bookApilogPath/ {print $2}' $BOOK_API_DIR/build_config.txt)


echo "testServerIP=$TEST_APP_CONTAINER_IP" >> /etc/environment
echo "testDatabaseIP=$TEST_MONGO_CONTAINER_IP" >> /etc/environment
echo "databaseIP=$MONGO_CONTAINER_IP" >> /etc/environment
echo "book_api_logs=$LOG_PATH" >> /etc/environment
