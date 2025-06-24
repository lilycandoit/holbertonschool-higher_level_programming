-- number of shows by genre

SELECT tv_genres.name AS genre, COUNT(tv_g.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres AS tv_g ON tv_genres.id = tv_g.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;