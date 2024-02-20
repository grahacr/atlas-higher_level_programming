-- create database and table with unique auto generated non-null primary key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS states (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(256)
);