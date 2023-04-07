#!/bin/bash

### Install MySQL server
sudo apt update
sudo apt install mysql-server --yes
sudo systemctl start mysql.service

# Follow steps in https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
# to configure MySQL password

### Install tshark
sudo apt install tshark

### Create environment
conda create -n pcap_gpt python=3.9 --yes

### Activate environment
conda activate pcap_gpt

### Install requirements
pip install -r requirements.txt