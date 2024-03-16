-- 
USE hbtn_0d_usa;
CREATE DATABASE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    state_id INT FOREIGN KEY REFERENCES states(id) NOT NULL,
    name VARCHAR(256) NOT NULL
);