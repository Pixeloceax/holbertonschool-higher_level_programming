-- Temperatures #2
SELECT state, MAX(value) AS `max`
FROM `temperatures`
GROUP BY state
LIMIT 3;
