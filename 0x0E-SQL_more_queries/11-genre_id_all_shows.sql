-- Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
SELECT t.`title`, g.`genre_id`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS g
ON t.`id` = g.`show_id`
ORDER BY t.`title`, g.`genre_id`;