import csv
import os

def save_movie(movie):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'user_movies.csv')

    fieldnames = [
        "title",
        "genre",
        "action",
        "humor",
        "romance",
        "emotion",
        "intensity",
        "duration",
        "family_friendly",
        "dark",
        "liked",
        "image"
    ]

    file_exists = os.path.isfile(file_path)

    movie_to_save = {
        "title": movie.get("title", ""),
        "genre": movie.get("genre", ""),
        "action": movie.get("action", 0),
        "humor": movie.get("humor", 0),
        "romance": movie.get("romance", 0),
        "emotion": movie.get("emotion", 0),
        "intensity": movie.get("intensity", 0),
        "duration": movie.get("duration", 0),
        "family_friendly": movie.get("family_friendly", 0),
        "dark": movie.get("dark", 0),
        "liked": movie.get("liked", 0),
        "image": movie.get("image", "")
    }

    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists or os.path.getsize(file_path) == 0:
            writer.writeheader()

        writer.writerow(movie_to_save)