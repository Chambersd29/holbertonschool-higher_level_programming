-- lists all shows contained in hbtn_0d_tvshows without a genre linked
-- each record should display: tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ASC order by tv_shows.title and tv_show_genres.genre_id
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
