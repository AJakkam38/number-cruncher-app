CREATE DATABASE IF NOT EXISTS calculations;
USE calculations;

CREATE TABLE IF NOT EXISTS executions (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_num INT unsigned NOT NULL,
    operator VARCHAR(1) NOT NULL,
    second_num INT unsigned NOT NULL,
    result INT unsigned NOT NULL
) AUTO_INCREMENT = 1;
