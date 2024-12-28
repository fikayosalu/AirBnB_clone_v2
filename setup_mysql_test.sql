-- A Scripts that prepares a MySQL server for Airbnb clone project tests
-- Creates a database, new user, and sets user privileges

-- Create a database hbnb_test_db, if it already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user hbnb_test, if it already exists, script should not fail
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to hbnb_dev on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to hbnb_dev on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
