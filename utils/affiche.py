from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_POSTER = ROOT / "assets" / "pas_d_image_disponible.png"

def afficher_affiche(film, width=200):
    if (film.get("image") or "").strip() != "":
        st.image(film["image"], width=width)
    else:
        st.image(str(DEFAULT_POSTER), width=width)