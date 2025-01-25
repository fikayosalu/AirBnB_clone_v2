#!/usr/bin/env bash
# Configure nginx
# Install Nginx if not installed
if ! command -v nginx &> /dev/null; then
    sudo apt update -y
    sudo apt install -y nginx
fi

# Create required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html><head></head><body><h1>Test Page</h1></body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create (or recreate) symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="\
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }"

if ! grep -q "hbnb_static" /etc/nginx/sites-available/default; then
    sudo sed -i "/server_name _;/a $nginx_config" /etc/nginx/sites-available/default
fi

# Restart Nginx to apply changes
sudo systemctl restart nginx

echo "Setup complete! Web static content is now available at /hbnb_static/"

