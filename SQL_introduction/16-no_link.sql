-- list all records of second_table with name value in certain order

SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;