from dotenv import load_dotenv
import os
import csv
import requests
import random

load_dotenv()

TOKEN = os.getenv("TMDB_BEARER_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json"
}

POPULAR_URL = "https://api.themoviedb.org/3/movie/popular"
DETAILS_URL = "https://api.themoviedb.org/3/movie"
GENRES_URL = "https://api.themoviedb.org/3/genre/movie/list"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

OUTPUT_FILE = "data/movies.csv"

FIELDNAMES = [
    "tmdb_id",
    "title",
    "year",
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

def get_genre_map():
    response = requests.get(GENRES_URL, headers=HEADERS, params={"language": "fr"})
    data = response.json()

    genre_map = {}
    for genre in data.get("genres", []):
        genre_map[genre["id"]] = genre["name"]

    return genre_map

def get_popular_movies(pages=2):
    movies = []

    for page in range(1, pages + 1):
        response = requests.get(
            POPULAR_URL,
            headers=HEADERS,
            params={"language": "fr-FR", "page": page}
        )
        data = response.json()
        movies.extend(data.get("results", []))

    return movies

def build_image_url(poster_path):
    if not poster_path:
        return ""
    return IMAGE_BASE + poster_path

def pick_main_genre(movie, genre_map):
    genre_ids = movie.get("genre_ids", [])
    if not genre_ids:
        return ""
    return genre_map.get(genre_ids[0], "")

def random_profile(main_genre, runtime):
    # Valeurs par défaut
    action = random.randint(2, 6)
    humor = random.randint(2, 6)
    romance = random.randint(2, 6)
    emotion = random.randint(3, 7)
    intensity = random.randint(3, 7)
    family_friendly = 0
    dark = random.randint(2, 6)

    genre_lower = main_genre.lower()

    if "action" in genre_lower or "aventure" in genre_lower:
        action = random.randint(7, 10)
        intensity = random.randint(7, 10)

    if "comédie" in genre_lower:
        humor = random.randint(7, 10)
        dark = random.randint(1, 4)

    if "romance" in genre_lower:
        romance = random.randint(7, 10)
        emotion = random.randint(6, 9)

    if "animation" in genre_lower or "famil" in genre_lower:
        family_friendly = 1
        dark = random.randint(1, 3)
        humor = max(humor, random.randint(5, 8))

    if "horreur" in genre_lower or "thriller" in genre_lower:
        dark = random.randint(7, 10)
        intensity = max(intensity, random.randint(6, 9))

    if "drame" in genre_lower:
        emotion = random.randint(7, 10)

    liked = random.choice([0, 1])

    return {
        "action": action,
        "humor": humor,
        "romance": romance,
        "emotion": emotion,
        "intensity": intensity,
        "duration": runtime if runtime else random.randint(80, 160),
        "family_friendly": family_friendly,
        "dark": dark,
        "liked": liked
    }

def fetch_runtime(movie_id):
    response = requests.get(
        f"{DETAILS_URL}/{movie_id}",
        headers=HEADERS,
        params={"language": "fr-FR"}
    )
    data = response.json()
    return data.get("runtime", 0)

def build_csv(sample_size=70):
    genre_map = get_genre_map()
    popular_movies = get_popular_movies(pages=3)

    seen_ids = set()
    rows = []

    for movie in popular_movies:
        movie_id = movie["id"]

        if movie_id in seen_ids:
            continue

        seen_ids.add(movie_id)

        title = movie.get("title", "").strip()
        release_date = movie.get("release_date", "")
        year = release_date[:4] if release_date else ""
        genre = pick_main_genre(movie, genre_map)
        poster_url = build_image_url(movie.get("poster_path"))
        runtime = fetch_runtime(movie_id)

        profile = random_profile(genre, runtime)

        row = {
            "tmdb_id": movie_id,
            "title": title,
            "year": year,
            "genre": genre,
            "action": profile["action"],
            "humor": profile["humor"],
            "romance": profile["romance"],
            "emotion": profile["emotion"],
            "intensity": profile["intensity"],
            "duration": profile["duration"],
            "family_friendly": profile["family_friendly"],
            "dark": profile["dark"],
            "liked": profile["liked"],
            "image": poster_url
        }

        rows.append(row)

        if len(rows) >= sample_size:
            break

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"{len(rows)} films écrits dans {OUTPUT_FILE}")

build_csv()