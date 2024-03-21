
#!/usr/bin/env python3
# script gets MySQL installed on both my web-01 and web-02 servers.
from fabric.api import * 
env.hosts=["34.227.93.198","54.166.169.232","34.232.65.82"]
env.key_filename=r"C:\Users\ahmed\.ssh\pk3.pem"
env.user="ubuntu"
# user="holberton_user"
# localhost="localhost"
# password=""
user="replica_user"
localhost="%"
password=""

sudo(f"""echo "CREATE USER '{user}'@'{localhost}' IDENTIFIED BY '{password}';" | mysql -u root -p""")

sudo(f"""echo "GRANT REPLICATION CLIENT ON *.* TO '{user}'@'{localhost}';" | mysql -u root -p""")
sudo(f""" echo "GRANT REPLICATION SLAVE ON *.* TO '{user}'@'{localhost}';" |  mysql -u root -p""")
sudo(f"""echo "GRANT ALL PRIVILEGES ON *.* TO '{user}'@'{localhost}'; FLUSH PRIVILEGES;" | mysql -u root -p""")
sudo("""echo "SELECT user, host FROM mysql.user;" | mysql -u root -p""")
