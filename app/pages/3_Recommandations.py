import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from utils.loadmovies import loadmovies
from utils.loaduserdata import load_user_data
from models.knn import kNN

st.title("Recommandation k-NN")
movies = loadmovies()

if mode == "Base fixe":
    movies = loadmovies()
else:
    movies = load_user_data()

    if len(movies) < 5:
        st.warning("Ajoute des films dans 'Base utilisateur'")
        st.stop()

action = st.slider("Action", 0, 10)
humor = st.slider("Humour", 0, 10)
romance = st.slider("Romance", 0, 10)
emotion = st.slider("Émotion", 0, 10)
intensity = st.slider("Intensité", 0, 10)
duration = st.slider("Durée", 60, 180)
family = st.selectbox("Familial", [0, 1])
dark = st.selectbox("Sombre", [0, 1])

k = st.slider("k", 1, 10)

if st.button("Prédire"):

    vect = [
        action,
        humor,
        romance,
        emotion,
        intensity,
        duration,
        family,
        dark
    ]

    Z = []
    for m in movies:
        Z.append({
            "vect": [
                m["action"],
                m["humor"],
                m["romance"],
                m["emotion"],
                m["intensity"],
                m["duration"],
                m["family_friendly"],
                m["dark"]
            ],
            "title": m["title"],
            "liked": m["liked"]
        })

    moyenne_dist = kNN(Z, k, vect)

    if moyenne_dist < 0.3:
        st.success("Très bon match")
    elif moyenne_dist < 0.6:
        st.warning("Match moyen")
    else:
        st.error("Pas recommandé")
    
    likes = sum(m["liked"] for m in movies)
    st.write("Films aimés :", likes)
    st.write("Total :", len(movies))
    