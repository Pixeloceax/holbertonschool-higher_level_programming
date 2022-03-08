-- Temperatures #0
SELECT `city`, AVG(`value`) AS `average`
FROM `temperatures`
GROUP BY `city`
ORDER BY `average` DESC;
