import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from pathlib import Path

from utils.loadmovies import loadmovies
from models.kmoy import k_moyennes

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_POSTER = ROOT / "assets" / "pas_d_image_disponible.png"

def afficher_affiche(film, width=140):
    image = (film.get("image") or "").strip()

    if image.startswith("http://") or image.startswith("https://"):
        st.image(image, width=width)
    elif image != "":
        st.image(image, width=width)
    else:
        st.image(str(DEFAULT_POSTER), width=width)

st.title("Groupes de films")
st.write("Cette page utilisera l'algorithme des k-moyennes afin de regrouper automatiquement les films en plusieurs catégories.")

movies = loadmovies()
k = st.slider("Choisis le nombre de groupes", 2, 6, 3)

if st.button("Lancer le clustering"):
    c, clus = k_moyennes(movies, k)

    st.success(f"{k} groupes ont été crées")

    for i in range(len(clus)):
        with st.expander(f"Groupe {i+1} ({len(clus[i])})"):
            if clus[i] == []:
                st.write("Aucun film dans ce groupe.")
            else:
                for film in clus[i]:
                    st.write("### " + film.get("title", "Titre inconnu"))
                    afficher_affiche(film, width=140)