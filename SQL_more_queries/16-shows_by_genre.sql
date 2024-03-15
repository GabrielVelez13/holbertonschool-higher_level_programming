-- lists all tv shows and their genres, if they have one
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre ASC;