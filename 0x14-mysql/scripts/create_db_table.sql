-- create a database and a new user
CREATE DATABASE
        IF NOT EXISTS `tyrell_corp`;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6
        (id INT NOT NULL, name VARCHAR(256) NOT NULL);
INSERT INTO nexus6 VALUE (1, "Shehab Negm");
GRANT SELECT
        on `nexus6`
        to 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
