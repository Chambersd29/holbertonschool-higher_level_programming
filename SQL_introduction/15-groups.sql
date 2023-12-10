-- Enumera el núero de registros con la misma puntuación
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
