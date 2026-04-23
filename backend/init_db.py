import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT,
    language TEXT,
    rating REAL,
    release_year INTEGER
)
""")

conn.commit()
conn.close()

print("Database created successfully")