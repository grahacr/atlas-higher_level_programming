-- list all genres and count of linked shows

SELECT tv_genres.name AS genre,
COUNT (tv_show_genres.genre_id) as number_of_shows
FROM tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name ORDER BY number_of_shows DESC;