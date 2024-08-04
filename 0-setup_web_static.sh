#!/usr/bin/env bash
# Script that prepares web servers for the deployment of web_static.

# Update and install nginx if it is not already installed
sudo apt-get update -y > /dev/null
sudo apt-get install nginx -y > /dev/null
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a simple HTML file to test Nginx configuration
echo 'hElLo, WoRlD' | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link, forcefully replacing it if it already exists
ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of the /data/ folder recursively to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/ > /dev/null

# Define the Nginx location block to handle /hbnb_static requests
new_block="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
marker="### HBNB_STATIC_MARKER ###"

# Check if the marker is already in the Nginx configuration file
if ! grep -q "$marker" /etc/nginx/sites-enabled/default && ! grep -q "location /hbnb_static/ {" /etc/nginx/sites-enabled/default; then
    # Insert the marker before the first occurrence of 'location / {'
    sudo sed -i "0,/location \/ {/s//${marker}\n&/" /etc/nginx/sites-enabled/default
fi

# Insert the location block before the marker and then remove the marker
sudo sed -i "/${marker}/i\\$new_block\n" /etc/nginx/sites-enabled/default
sudo sed -i "/${marker}/d" /etc/nginx/sites-enabled/default

# Restart Nginx to apply the changes
sudo service nginx restart > /dev/null
