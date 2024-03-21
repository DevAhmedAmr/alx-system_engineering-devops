#!/usr/bin/env python3
# script gets MySQL installed on both my web-01 and web-02 servers.
from fabric.api import * 
env.hosts=["34.227.93.198","54.166.169.232","34.232.65.82"]
env.key_filename=r"C:\Users\ahmed\.ssh\pk3.pem"
env.user="ubuntu"
#these configurations are done based on this tutorial
#? https://www.fosstechnix.com/how-to-install-mysql-5-7-on-ubuntu-22-04-lts/
# sudo("apt update -y")
# sudo("sudo apt install wget -y")
# run("wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb")
# run("sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb")

# run("echo --------step2-------")
#? sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
# sudo("sudo apt-get update")
# sudo("apt-cache policy mysql-server")
# sudo("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29")
# sudo("apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*")
# sudo("sudo mysql_secure_installation")
#run("mysql -u root -p ")

#configure sql package
#?sudo dpkg-reconfigure mysql-apt-config
