-- Temperatures #2
SELECT `State`, MAX(value) AS `max_temp`
FROM `temperatures`
GROUP BY `State`
LIMIT 3;
