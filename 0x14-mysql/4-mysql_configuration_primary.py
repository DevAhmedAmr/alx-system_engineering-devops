#!/usr/bin/env python3
# script gets MySQL installed on both my web-01 and web-02 servers.
from fabric.api import * 
from check_and_update_config_line import check_and_update_config_line

env.hosts=["34.227.93.198","54.166.169.232","34.232.65.82"]
env.key_filename=r"C:\Users\ahmed\.ssh\pk3.pem"
env.user="ubuntu"
file_path="/etc/mysql/mysql.conf.d/mysqld.cnf"
database_name="tyrell_corp"


# sudo("ufw allow from 54.166.169.232 to any port 3306")

check_and_update_config_line("bind-address","# bind-address = 127.0.0.1",file_path)
check_and_update_config_line("server-id","server-id = 1",file_path)
check_and_update_config_line("log_bin","log_bin = /var/log/mysql/mysql-bin.log",file_path)
check_and_update_config_line("binlog_do_db",f"binlog_do_db = {database_name}",file_path)
sudo("sudo systemctl restart mysql")

sudo("echo 'FLUSH TABLES WITH READ LOCK;' | mysql -u root -p")
sudo("echo 'SHOW MASTER STATUS;' | mysql -u root -p")
sudo(f"mysqldump -u root -p {database_name} > {database_name}.sql")
sudo("echo 'UNLOCK TABLES;' | mysql -u root -p")
get(f"./{database_name}.sql",r"S:\alx\alx-system_engineering-devops\0x14-mysql\sql")








# Search for the line containing the word "bind-address" and comment it out
# sudo (f"""sed -i '/bind-address/ s/^/#/' {file_path} """)
# print("bind-address line commented out.")
# sudo(f"""sed -i '/# server-id = 1/ s/^#//' {file_path}""")
# print( "# server-id  Line uncommented.")

# sudo(f"""sed -i '/# log_bin = \/var\/log\/mysql\/mysql-bin.log/ s/^#//' {file_path}""")
# print("# log_bin   Line uncommented.")

# sudo(f"""sed -i '/# binlog_do_db = include_database_name/ s/^# //' {file_path}""")
# sudo(f"""sed -i 's/include_database_name/{database_name}/' {file_path}""")

# print( "' #binlog_do_db = include_database_name' Line uncommented and replaced.")

