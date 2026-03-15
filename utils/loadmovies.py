import csv
import os 

def loadmovies():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'data', 'movies.csv')
    
    movies = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            movie = {
                "title": row["title"],
                "genre": row["genre"],
                "action": int(row["action"]),
                "humor": int(row["humor"]),
                "romance": int(row["romance"]),
                "emotion": int(row["emotion"]),
                "intensity": int(row["intensity"]),
                "duration": int(row["duration"]),
                "family_friendly": int(row["family_friendly"]),
                "dark": int(row["dark"]),
                "liked": int(row["liked"])
            }
            movies.append(movie)
    
    return movies 
