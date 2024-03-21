
#!/usr/bin/env python3
# script gets MySQL installed on both my web-01 and web-02 servers.
from fabric.api import * 
env.hosts=["34.227.93.198","54.166.169.232","34.232.65.82"]
env.key_filename=r"C:\Users\ahmed\.ssh\pk3.pem"
env.user="ubuntu"
run("echo 'CREATE DATABASE tyrell_corp;' | mysql -u root -p ")
run("echo 'CREATE TABLE nexus6 (id int, name varchar(255) );' | mysql -u root -p tyrell_corp")
run("""echo "INSERT INTO nexus6 (id , name) values (4 , 'ibrahim')" | mysql -u root -p tyrell_corp""")
run(""" mysql -u root -p -e "use tyrell_corp; select * from nexus6" """)