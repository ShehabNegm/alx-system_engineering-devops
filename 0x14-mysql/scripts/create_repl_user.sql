-- create new user on SQL server
-- user will graned REPLICATION SLAVE
CREATE USER
        IF NOT EXISTS 'replica_user'@'%'
        IDENTIFIED BY 'rep';
GRANT REPLICATION SLAVE
        ON *.*
        TO 'replica_user'@'%';
GRANT SELECT
        ON mysql.user
        TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
