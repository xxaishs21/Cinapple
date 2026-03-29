import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from utils.loadmovies import loadmovies

st.title("Groupes de films")
st.write("Cette page utilisera l'algorithme des k-moyennes.")