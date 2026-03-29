import streamlit as st

from utils.loadmovies import loadmovies
from models.knn import kNN

def render():
    st.title("Recommandation k-NN")
    st.write("Cette page utilisera l'algorithme des k plus proches voisins (k-NN).")
