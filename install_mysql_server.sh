#!/bin/bash

sudo apt update
sudo apt install mysql-server --yes
sudo systemctl start mysql.service

# Follow steps in https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
# to configure MySQL password