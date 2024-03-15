-- create a table where id defaults to 1.
CREATE table if NOT EXISTS id_not_null(
    id INT default 1,
    name VARCHAR(256)
);
