import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import random
from utils.loadmovies import loadmovies
from utils.saveuserdata import save_movie

st.title("Construire ma base de préférences")

st.write("""
Pour une expérience personnalisée, avant d'utiliser les algorithmes, tu dois noter des films.
Plus tu notes de films, plus les recommandations seront précises.
""")

if "user_data" not in st.session_state:
    st.session_state.user_data = []

if "current_movie" not in st.session_state:
    movies = loadmovies()
    st.session_state.current_movie = random.choice(movies)

movie = st.session_state.current_movie

st.subheader(movie["title"])

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👍 J'aime"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 1
        save_movie(movie_copy)  
        st.session_state.current_movie = random.choice(loadmovies())

with col2:
    if st.button("👎 J'aime pas"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 0
        save_movie(movie_copy)  
        st.session_state.current_movie = random.choice(loadmovies())

with col3:
    if st.button("⏭️ Pas vu"):
        st.session_state.current_movie = random.choice(loadmovies())


if st.button("Réinitialiser mes données"):
    open("data/user_movies.csv", "w").close()