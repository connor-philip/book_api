SETUP_SCRIPTS_DIR="${0%/*}"
ENVIRONMENT_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
DOCKER_SUB_NET=$(grep dockerSubNet $BOOK_API_DIR/build_config.txt | grep -Po '((?:\d{1,3}\.){3}\d{1,3})')

docker network ls | grep booknet || docker network create --subnet=$DOCKER_SUB_NET/16 booknet
