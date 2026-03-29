import csv
import os

def save_movie(movie):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'user_movies.csv')

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=movie.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(movie)