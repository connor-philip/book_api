#!/bin/bash

container=$1
fullContainerName=book_api_$container

if [[ $container == "app" ]]; then
    docker ps | grep book_api_app && docker kill $fullContainerName
    docker ps -a | grep book_api_app && docker rm $fullContainerName
elif [[ $container == "db" ]]; then
    docker ps | grep book_api_db && docker kill $fullContainerName
    docker ps -a | grep book_api_db && docker rm $fullContainerName
else
    echo "Invalid parameter supplied."
    echo "Run the script with adding either app or db as an argument"
    echo "e.g. bash kill_remove_container app"
    exit 1
fi
