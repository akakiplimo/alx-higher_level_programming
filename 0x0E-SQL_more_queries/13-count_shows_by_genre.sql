-- 13-count_shows_by_genre.sql
SELECT tv_genres.name AS genre,
       COUNT(show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres AS show_genres
ON tv_genres.id = show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC
