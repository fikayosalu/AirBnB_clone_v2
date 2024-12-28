-- A Scripts that prepares a MySQL server for Airbnb clone project:
-- Creates a database, new user, and sets user privileges

-- Create a database hbnb_dev_db, if it already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user hbnb_dev, if it already exists, script should not fail
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to hbnb_dev on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege to hbnb_dev on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
