import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import random
from pathlib import Path

from utils.loadmovies import loadmovies
from utils.loadusermovies import load_user_data
from utils.saveuserdata import save_movie

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_POSTER = ROOT / "assets" / "pas_d_image_disponible.png"

def afficher_affiche(film, width=220):
    image = (film.get("image") or "").strip()

    if image != "":
        st.image(image, width=width)
    else:
        st.image(str(DEFAULT_POSTER), width=width)

def films_restants():
    all_movies = loadmovies()
    user_movies = load_user_data()

    titres_deja_notes = set()
    for film in user_movies:
        titres_deja_notes.add(film["title"])

    titres_passes = st.session_state.get("passed_titles", set())

    restants = []
    for film in all_movies:
        if film["title"] not in titres_deja_notes and film["title"] not in titres_passes:
            restants.append(film)

    return restants

st.title("Construire ma base de préférences")

st.write("""
Pour une expérience personnalisée, avant d'utiliser les algorithmes, tu dois noter des films.
Plus tu notes de films, plus les recommandations seront précises.
""")

if "passed_titles" not in st.session_state:
    st.session_state["passed_titles"] = set()

movies = films_restants()

if movies == []:
    st.success("Tu as déjà parcouru tous les films disponibles.")
    st.stop()

if "current_movie_title" not in st.session_state:
    st.session_state["current_movie_title"] = random.choice(movies)["title"]

movie = None
for f in movies:
    if f["title"] == st.session_state["current_movie_title"]:
        movie = f
        break

if movie is None:
    movie = random.choice(movies)
    st.session_state["current_movie_title"] = movie["title"]

st.subheader(movie["title"])
afficher_affiche(movie, width=220)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👍 J'aime"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 1
        save_movie(movie_copy)

        nouveaux_movies = films_restants()
        if nouveaux_movies != []:
            st.session_state["current_movie_title"] = random.choice(nouveaux_movies)["title"]
        else:
            st.session_state.pop("current_movie_title", None)

        st.rerun()

with col2:
    if st.button("👎 J'aime pas"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 0
        save_movie(movie_copy)

        nouveaux_movies = films_restants()
        if nouveaux_movies != []:
            st.session_state["current_movie_title"] = random.choice(nouveaux_movies)["title"]
        else:
            st.session_state.pop("current_movie_title", None)

        st.rerun()

with col3:
    if st.button("⏭️ Pas vu"):
        st.session_state["passed_titles"].add(movie["title"])

        nouveaux_movies = films_restants()
        if nouveaux_movies != []:
            st.session_state["current_movie_title"] = random.choice(nouveaux_movies)["title"]
        else:
            st.session_state.pop("current_movie_title", None)

        st.rerun()

if st.button("Réinitialiser mes données"):
    with open("data/user_movies.csv", "w", encoding="utf-8") as f:
        f.write("title,genre,action,humor,romance,emotion,intensity,duration,family_friendly,dark,liked,image\n")

    st.session_state["passed_titles"] = set()
    st.session_state.pop("current_movie_title", None)
    st.rerun()