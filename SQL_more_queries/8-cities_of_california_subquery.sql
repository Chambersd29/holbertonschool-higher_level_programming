--Enumera todas las ciudades de California
SELECT id FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = "California"
)
ORDER BY id;
