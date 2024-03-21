#!/usr/bin/env python3
from fabric.api import * 
env.hosts=["34.227.93.198","54.166.169.232","34.232.65.82"]
env.key_filename=r"C:\Users\ahmed\.ssh\pk3.pem"
env.user="ubuntu"

"""code to append the public key to my servers """

public_key="""ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
"""
# Create a directory for the user's SSH keys if it doesn't exist
sudo(f"mkdir -p /home/{env.user}/.ssh")

# Create an empty authorized_keys file if it doesn't exist
sudo(f"touch /home/{env.user}/.ssh/authorized_keys")

# Set permissions for the .ssh directory
sudo(f"chmod 700 /home/{env.user}/.ssh")

# Set permissions for the authorized_keys file
sudo(f"chmod 600 /home/{env.user}/.ssh/authorized_keys")

# Append the public_key to the authorized_keys file
sudo(f"echo '{public_key}' >> /home/{env.user}/.ssh/authorized_keys")

# Change ownership of the .ssh directory and authorized_keys file to the user
sudo(f"chown -R {env.user}:{env.user} /home/{env.user}/.ssh")
