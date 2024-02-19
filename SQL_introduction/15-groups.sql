-- list count of records with same score in second_table in certain order

SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
GROUP BY number DESC;