-- create mysql server for application --

-- create main db --
CREATE DATABASE IF NOT EXISTS hbnb_dev db;

-- create main user --
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- user has full priviledges on main db --
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- select priviledge for user on performance schema db --
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
