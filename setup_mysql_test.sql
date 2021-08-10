-- prepare a MYSQL testing environment --

-- Create testing database --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create test user --
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- test user will have full priviledges on test db --
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- test user will have select priviledges on performance schema  table --
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
