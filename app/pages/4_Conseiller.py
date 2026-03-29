import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from utils.loadmovies import loadmovies

st.title("Conseiller ID3")
st.write("Cette page utilisera l'arbre de décision ID3.")