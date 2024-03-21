#!/usr/bin/env python3
# Importing necessary modules
from fabric.api import * 

# Defining the host servers
env.hosts = ["34.227.93.198", "54.166.169.232", "34.232.65.82"]

# Setting the SSH key file location and the username for SSH connection
env.key_filename = r"C:\Users\ahmed\.ssh\pk3.pem"
env.user = "ubuntu"

# Database name and table name variables
dataBase_name = "tyrell_corp"
table_name = "nexus6"

# Creating the database
run(f"echo 'CREATE DATABASE {dataBase_name};' | mysql -u root -p ")

# Creating a table in the database
run(f"echo 'CREATE TABLE {table_name} (id int, name varchar(255) );' | mysql -u root -p tyrell_corp")

# Inserting data into the table
run(f"""echo "INSERT INTO {table_name} (id , name) values (4 , 'ibrahim')" | mysql -u root -p tyrell_corp""")

# Querying the database to display the inserted data
run(f""" mysql -u root -p -e "use {dataBase_name}; select * from {table_name}" """)
