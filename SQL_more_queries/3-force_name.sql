-- create table force_name which must have name

CREATE table IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);