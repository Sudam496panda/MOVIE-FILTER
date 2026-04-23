DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS movie_genres;
DROP TABLE IF EXISTS movie_languages;

CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    rating REAL,
    release_year INTEGER
);

CREATE TABLE genres (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE languages (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE movie_genres (
    movie_id INTEGER,
    genre_id INTEGER
);

CREATE TABLE movie_languages (
    movie_id INTEGER,
    language_id INTEGER
);

-- Indexing (CRITICAL)
CREATE INDEX idx_mg ON movie_genres(genre_id, movie_id);
CREATE INDEX idx_ml ON movie_languages(language_id, movie_id);
CREATE INDEX idx_rating ON movies(rating);