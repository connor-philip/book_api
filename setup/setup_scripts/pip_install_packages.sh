#!/bin/bash

SETUP_SCRIPTS_DIR="${0%/*}"
SETUP_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$SETUP_DIR/..

cd $BOOK_API_DIR

pip3 install .
pip3 install pymongo
pip3 install flask

cd -
