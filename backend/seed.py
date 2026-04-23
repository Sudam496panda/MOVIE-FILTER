import sqlite3
import random

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# CREATE TABLES
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    rating REAL,
    release_year INTEGER
)
""")

# INSERT SAMPLE DATA
for i in range(1,51):
    cursor.execute("""
    INSERT INTO movies (title, rating, release_year)
    VALUES (?, ?, ?)
    """, (f"Movie {i}", round(random.uniform(5, 9), 1), 2020 + (i % 5)))

conn.commit()
conn.close()

print("Database created successfully")