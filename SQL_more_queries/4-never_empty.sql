-- create table with default value in id column

CREATE table IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);