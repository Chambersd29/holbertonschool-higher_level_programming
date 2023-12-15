-- lists all the cities of California that can be found on the database 'hbtn_0d_usa'
-- the states table contains only one record where name = California, but id can be different 
-- results must be sorted in ascending order by cities.id
-- is not allowed to use JOIN kw
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = "California"
)
ORDER BY id;
