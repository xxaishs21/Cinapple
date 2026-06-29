from dotenv import load_dotenv
import os
import csv
import requests

load_dotenv()

TOKEN = os.getenv("TMDB_BEARER_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json"
}

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

def get_poster_url(title):
    params = {
        "query": title,
        "language": "en-US",
        "page": 1
    }

    response = requests.get(SEARCH_URL, headers=HEADERS, params=params)
    data = response.json()

    results = data.get("results", [])
    if not results:
        return ""

    poster_path = results[0].get("poster_path")
    if not poster_path:
        return ""

    return IMAGE_BASE + poster_path

def fill_images_in_csv(input_file="data/movies.csv", output_file="data/movies.csv"):
    rows = []

    with open(input_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        if "image" not in fieldnames:
            fieldnames.append("image")

        for row in reader:
            if not row.get("image"):
                print("Recherche :", row["title"])
                row["image"] = get_poster_url(row["title"])
                print(" ->", row["image"])
            rows.append(row)

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

fill_images_in_csv()