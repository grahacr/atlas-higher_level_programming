-- list cities in database ascending order

SELECT cities.id, cities.name, states.name
FROM cities JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;