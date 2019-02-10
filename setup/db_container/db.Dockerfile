FROM ubuntu:16.04
LABEL maintainer="connor.philip12@hotmail.com"

USER root

COPY setup/setup_scripts/ /var/setup/setup_scripts

# Install and setup MongoDB
RUN ["bash", "/var/setup/setup_scripts/apt_install_mongodb.sh"]
RUN mkdir -p /data/db
RUN mkdir -p /data/configdb
VOLUME /data/db /data/configdb

EXPOSE 27017

ENTRYPOINT /usr/bin/mongod