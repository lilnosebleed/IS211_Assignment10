-- creates the artists table (we only need the artist's name)
CREATE TABLE artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

-- creates the albums table and links it to the artist who created it
CREATE TABLE albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
);

-- creates the songs table with track numbers and lengths, linked to an album
CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    album_id INTEGER,
    track_number INTEGER,
    length_in_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(id)
);
