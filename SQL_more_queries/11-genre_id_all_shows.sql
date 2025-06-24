-- Genre ID for all shows

SELECT tv_s.title, tv_g.genre_id
FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_g ON tv_s.id = tv_g.show_id
ORDER BY tv_s.title, tv_g.genre_id;