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

    restants = []
    for film in all_movies:
        if film["title"] not in titres_deja_notes:
            restants.append(film)

    return restants

st.title("Construire ma base de préférences")

st.write("""
Pour une expérience personnalisée, avant d'utiliser les algorithmes, tu dois noter des films.
Plus tu notes de films, plus les recommandations seront précises.
""")

movies = films_restants()

if movies == []:
    st.success("Tu as déjà parcouru tous les films disponibles.")
    st.stop()

if "current_movie_index" not in st.session_state:
    st.session_state.current_movie_index = random.randrange(len(movies))

if st.session_state.current_movie_index >= len(movies):
    st.session_state.current_movie_index = random.randrange(len(movies))

movie = movies[st.session_state.current_movie_index]

st.subheader(movie["title"])
afficher_affiche(movie, width=220)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👍 J'aime"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 1
        save_movie(movie_copy)

        nouveaux_movies = films_restants()
        if nouveaux_movies == []:
            st.session_state.pop("current_movie_index", None)
        else:
            st.session_state.current_movie_index = random.randrange(len(nouveaux_movies))
        st.rerun()

with col2:
    if st.button("👎 J'aime pas"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 0
        save_movie(movie_copy)

        nouveaux_movies = films_restants()
        if nouveaux_movies == []:
            st.session_state.pop("current_movie_index", None)
        else:
            st.session_state.current_movie_index = random.randrange(len(nouveaux_movies))
        st.rerun()

with col3:
    if st.button("⏭️ Pas vu"):
        if len(movies) > 1:
            nouvel_index = st.session_state.current_movie_index
            while nouvel_index == st.session_state.current_movie_index:
                nouvel_index = random.randrange(len(movies))
            st.session_state.current_movie_index = nouvel_index
        st.rerun()

if st.button("Réinitialiser mes données"):
    with open("data/user_movies.csv", "w", encoding="utf-8") as f:
        f.write("title,genre,action,humor,romance,emotion,intensity,duration,family_friendly,dark,liked,image\n")
    st.session_state.pop("current_movie_index", None)
    st.rerun()