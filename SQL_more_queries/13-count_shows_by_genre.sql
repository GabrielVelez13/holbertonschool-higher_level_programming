-- Count shows by genre
SELECT genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;