import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import streamlit as st
from my_pages import home, page_knn, page_id3, page_kmoy

st.set_page_config(
    page_title="Cinapple",
    page_icon="🎬",
    layout="wide"
)

page = st.sidebar.radio(
    "**MENU**",
    ["Accueil", "Recommandation k-NN", "Conseiller ID3", "Groupes de films"]
)

if page == "Accueil" : 
    home.render()
elif page == "Recommandation k-NN" : 
    page_knn.render()
elif page == "Conseiller ID3" : 
    page_id3.render()
elif page == "Groupes de films" : 
    page_kmoy.render()
    