from fabric.api import * 
from check_and_update_config_line import check_and_update_config_line
env.host_string="54.166.169.232"
env.key_filename=r"C:\Users\ahmed\.ssh\pk3.pem"
env.user="ubuntu"
file_path="/etc/mysql/mysql.conf.d/mysqld.cnf"
database_name="tyrell_corp"
password=""


put(r"./sql/tyrell_corp.sql", r"/tmp/")
sudo("echo 'CREATE DATABASE tyrell_corp;' | mysql -u root -p")
sudo(f"mysql -u root -p {database_name} < /tmp/{database_name}.sql")
check_and_update_config_line("server-id","server-id = 2",file_path)
check_and_update_config_line("log_bin","log_bin = /var/log/mysql/mysql-bin.log",file_path)
check_and_update_config_line("binlog_do_db",f"binlog_do_db = {database_name}",file_path)
check_and_update_config_line("relay-log",f"relay-log = /var/log/mysql/mysql-relay-bin.log",file_path)
sudo("systemctl restart mysql")

mysql_command=f"""CHANGE MASTER TO 
MASTER_HOST='34.227.93.198'
,MASTER_USER='replica_user'
,MASTER_PASSWORD='{password}'
,MASTER_LOG_FILE='mysql-bin.000002'
,MASTER_LOG_POS=154;"""
sudo(f"""printf %s "{mysql_command}" | mysql -u root -p""")
sudo(f"printf %s 'START SLAVE;' | mysql -u root -p")
