#!/bin/bash

SETUP_SCRIPTS_DIR="${0%/*}"
ENVIRONMENT_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..

cd $BOOK_API_DIR

if [[ $1 == "dev_environment" ]]; then
        pip3 install -r dev_requirements.txt
else
    pip3 install -r requirements.txt
fi

cd -
