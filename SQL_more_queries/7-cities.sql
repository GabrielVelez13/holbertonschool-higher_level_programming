-- Create a table called cities with the following columns:
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
\c hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id SERIAL PRIMARY KEY,
    state_id INT REFERENCES states(id) NOT NULL,
    name VARCHAR(256) NOT NULL
);
