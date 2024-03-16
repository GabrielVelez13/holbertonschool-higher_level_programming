-- 
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
JOIN tv_show_genres ON hbtn_0d_tvshows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
