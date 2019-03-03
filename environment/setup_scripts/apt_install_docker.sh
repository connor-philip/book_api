#!/bin/bash

apt-get update
apt-get --no-install-recommends install curl
apt-get --no-install-recommends install apt-transport-https
apt-get --no-install-recommends install ca-certificates
apt-get --no-install-recommends install software-properties-common
curl -fsSL https://apt.dockerproject.org/gpg | sudo apt-key add -
add-apt-repository \
       "deb https://apt.dockerproject.org/repo/ \
       ubuntu-$(lsb_release -cs) \
       main"
apt-get update
apt-get -y install docker-engine=1.13.0-0~ubuntu-xenial
