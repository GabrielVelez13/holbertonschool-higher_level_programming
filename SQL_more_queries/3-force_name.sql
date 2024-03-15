-- Create table where the name is forced to be not null
CREATE table if NOT EXISTS force_name{
    id INT;
    name VARCHAR(256) NOT NULL;
}
