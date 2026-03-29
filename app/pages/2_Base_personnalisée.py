import streamlit as st
import random
from utils.loadmovies import loadmovies

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

col1, col2 = st.columns(2)

with col1:
    if st.button("👍 J'aime"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 1
        st.session_state.user_data.append(movie_copy)
        st.session_state.current_movie = random.choice(loadmovies())

with col2:
    if st.button("👎 J'aime pas"):
        movie_copy = movie.copy()
        movie_copy["liked"] = 0
        st.session_state.user_data.append(movie_copy)
        st.session_state.current_movie = random.choice(loadmovies())

st.write("Films notés :", len(st.session_state.user_data))