CREATE DATABASE IF NOT EXISTS blog_db;
CREATE USER IF NOT EXISTS 'dev'@'localhost' IDENTIFIED BY "$MYSQL_PWD";
GRANT ALL PRIVILEGES ON `blog_db`.* TO 'dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'dev'@'localhost';
FLUSH PRIVILEGES;
