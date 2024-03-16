-- Create a database and a table with the following requirements:
CREATE database if NOT EXISTS hbtn_0c_usa;
CREATE table if NOT EXISTS states(
    id INT UNIQUE SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
