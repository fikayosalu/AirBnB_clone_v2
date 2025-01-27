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
sudo sed -i "54a\\
	location /hbnb_static/ {\\
		alias /data/web_static/current;\\
	}" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

echo "Setup complete! Web static content is now available at /hbnb_static/"
