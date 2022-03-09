-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)
SELECT t.`title`, g.`genre_id`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS g
WHERE t.`id` = g.`show_id` IS NULL 
ORDER BY t.`title`, g.`genre_id`;
