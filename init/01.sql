CREATE DATABASE IF NOT EXISTS calculations;
USE calculations;

CREATE TABLE IF NOT EXISTS executions (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_num INT NOT NULL,
    operator VARCHAR(4) NOT NULL,
    second_num INT NOT NULL,
    result INT NOT NULL
) AUTO_INCREMENT = 1;
