CONTAINER_SCRIPTS_DIR="${0%/*}"
SETUP_DIR=$CONTAINER_SCRIPTS_DIR/..
BOOK_API_DIR=$SETUP_DIR/..
DOCKER_SUB_NET=$(grep dockerSubNet $BOOK_API_DIR/config.py | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

docker network ls | grep booknet || docker network create --subnet=$DOCKER_SUB_NET/16 booknet
