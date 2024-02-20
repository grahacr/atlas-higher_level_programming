-- cities of california in database hbtn_0d_usa

SELECT id, name FROM cities WHERE state_id = 
    (SELECT id from states where name = 'California')
ORDER BY cities.id ASC;