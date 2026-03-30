import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from utils.loadmovies import loadmovies
from models.kmoy import k_moyennes

st.title("Groupes de films")
st.write("Cette page utilisera l'algorithme des k-moyennes afin de regrouper automatiquement les films en plusieurs catégories.")

movies = loadmovies()
k = st.slider("Choisis le nombre de groupes", 2, 6, 3)

if st.button("Lancer le clustering"):
    c, clus = k_moyennes(movies, k)
    
    st.success(f"{k} groupes ont été crées")
    
    for i in range(len(clus)):
        with st.expander(f"Groupe {i+1} ({len(clus[i])})"):
            if clus[i]==[]:
                st.write("Aucun film dans ce groupe.")
            else:
                for film in clus[i]:
                    st.write("- " + film["title"])
      