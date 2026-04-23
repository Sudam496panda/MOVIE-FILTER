from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# DATABASE PATH
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "movies.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    return """ <div style="text-align:center; padding:30px; background:linear-gradient(135deg,#111,#333); color:white; border-radius:12px;">
      <img src="https://cdn.aptoide.com/imgs/1/4/4/14453f97dd347afb0766597fead58479_fgraphic.png" style="width:100%; max-height:320px; object-fit:cover; border-radius:12px;"> 
      <h1>🎬 Movie Filter API Running</h1> <p>Backend is active and ready</p>
        <button onclick="window.location.href='/movies'" style="background:#ff3d3d; color:white; padding:12px 22px; border:none; border-radius:8px;"> View Movies </button>
          </div> 
    """

# -----------------------------
# GET MOVIES (SORTED BY ID ASC)
# -----------------------------
@app.route("/movies", methods=["GET"])
def get_movies():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM movies
        ORDER BY id ASC
    """)

    movies = cursor.fetchall()
    conn.close()

    return jsonify([dict(m) for m in movies])


# -----------------------------
# ADD MOVIE
# -----------------------------
@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.get_json()

    title = data.get("title")
    genre = data.get("genre", "Action")
    language = data.get("language", "English")
    rating = data.get("rating")
    year = data.get("release_year")

    if not title or rating is None or year is None:
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies (title, genre, language, rating, release_year)
        VALUES (?, ?, ?, ?, ?)
    """, (title, genre, language, rating, year))

    conn.commit()
    conn.close()

    return jsonify({"message": "Movie added successfully"}), 201


# -----------------------------
# DELETE MOVIE
# -----------------------------
@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM movies WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Movie deleted"})


# -----------------------------
# RUN SERVER
# -----------------------------
# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)