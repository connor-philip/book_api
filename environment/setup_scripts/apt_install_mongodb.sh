#!/bin/bash

package=$1

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
apt-get update


if [[ $package == "client_only" ]]; then
    apt-get install -y mongodb-org-shell
    apt-get install -y mongodb-org-tools
else
    apt-get install -y mongodb-org
fi