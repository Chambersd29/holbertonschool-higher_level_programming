-- lists all genres contained in hbtn_0d_tvshows and the number of shows linked -- to each
-- each record should display:
-- <TV show genre> - <Number of shows linked tothis genre>

SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
