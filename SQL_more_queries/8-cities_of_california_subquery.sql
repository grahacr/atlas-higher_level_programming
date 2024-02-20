-- cities of california in database hbtn_0d_usa

SELECT 
(SELECT name FROM cities WHERE state_id = id) AS city
FROM states
ORDER BY cities.id ASC;