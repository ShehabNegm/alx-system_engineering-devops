#!/usr/bin/env bash
sudo apt-key add signature.key
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
sudo apt-get -y update
sudo apt install -f -y mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
