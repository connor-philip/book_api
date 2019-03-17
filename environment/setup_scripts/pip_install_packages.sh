#!/bin/bash

SETUP_SCRIPTS_DIR="${0%/*}"
ENVIRONMENT_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..

cd $BOOK_API_DIR


pip3 install -r requirements.txt


cd -
