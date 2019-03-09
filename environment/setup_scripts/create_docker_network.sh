SETUP_SCRIPTS_DIR="${0%/*}"
ENVIRONMENT_DIR=$SETUP_SCRIPTS_DIR/..
BOOK_API_DIR=$ENVIRONMENT_DIR/..
DOCKER_SUB_NET=$(awk '/dockerSubNet/ {print $2}' $BOOK_API_DIR/build_config.txt)

docker network ls | grep booknet || docker network create --subnet=$DOCKER_SUB_NET/16 booknet
