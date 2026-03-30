import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
from models.id3 import conv_class_id3, id3, features

st.title("Conseiller ID3")
st.write("Cette page utilise l'arbre de décision ID3.")
st.write("Réponds aux questions, et le conseiller te proposera des films correspondant à ton profil.")

movies_id3 = conv_class_id3()
tree = id3(movies_id3, features)

def question_from_attribute(attribute):
    questions = {
        "action": "Veux-tu de l'action ?",
        "humor": "Veux-tu quelque chose de drôle ?",
        "romance": "Veux-tu une histoire romantique ?",
        "emotion": "Cherches-tu un film émouvant ?",
        "intensity": "Veux-tu un film intense ?",
        "duration": "Quelle durée préfères-tu ?",
        "family_friendly": "Veux-tu un film familial ?",
        "dark": "Veux-tu un film plutôt sombre ?"
    }
    return questions.get(attribute, attribute)

def label_from_value(attribute, value):
    if attribute in ["action", "humor", "romance", "emotion", "intensity", "dark"]:
        labels = {
            "faible": "Pas vraiment",
            "moyen": "Un peu",
            "fort": "Beaucoup"
        }
        return labels.get(value, value)

    if attribute == "duration":
        labels = {
            "court": "Court",
            "moyen": "Moyen",
            "long": "Long"
        }
        return labels.get(value, value)

    if attribute == "family_friendly":
        labels = {
            "oui": "Oui",
            "non": "Non"
        }
        return labels.get(value, value)

    return value

def films_compatibles(movies, history):
    result = []

    for movie in movies:
        ok = True
        for attr, val in history:
            if movie[attr] != val:
                ok = False
                break
        if ok:
            result.append(movie)

    return result

if "node_id3" not in st.session_state:
    st.session_state["node_id3"] = tree

if "history_id3" not in st.session_state:
    st.session_state["history_id3"] = []

node = st.session_state["node_id3"]
history = st.session_state["history_id3"]

if node["type"] == "leaf":
    candidats = films_compatibles(movies_id3, history)

    if node["class"] == 1:
        st.success("Le conseiller a trouvé un profil qui semble correspondre à tes envies.")

        bons_films = []
        for film in candidats:
            if film["liked"] == 1:
                bons_films.append(film)

        if bons_films != []:
            st.write("### Films conseillés")
            for film in bons_films[:5]:
                st.write("- " + film["title"])
        else:
            st.write("Aucun film exact trouvé dans la base pour ce profil.")
    else:
        st.error("Ce profil semble moins correspondre à tes goûts.")

        if candidats != []:
            st.write("### Films correspondant au profil")
            for film in candidats[:5]:
                st.write("- " + film["title"])
        else:
            st.write("Aucun film exact trouvé dans la base pour ce profil.")

    if history != []:
        st.markdown("---")
        st.write("**Résumé de tes réponses :**")
        for attr, ans in history:
            st.write("- " + question_from_attribute(attr) + " → " + label_from_value(attr, ans))

    if st.button("Recommencer"):
        st.session_state["node_id3"] = tree
        st.session_state["history_id3"] = []
        st.rerun()

else:
    attribute = node["attribute"]
    question = question_from_attribute(attribute)
    values = list(node["children"].keys())

    display_map = {}
    display_choices = []

    for v in values:
        label = label_from_value(attribute, v)
        display_map[label] = v
        display_choices.append(label)

    st.write("### " + question)

    answer_label = st.radio("Choisis une réponse :", display_choices)
    answer_value = display_map[answer_label]

    if st.button("Valider"):
        st.session_state["history_id3"].append((attribute, answer_value))
        st.session_state["node_id3"] = node["children"][answer_value]
        st.rerun()

    if history != []:
        st.markdown("---")
        st.write("**Réponses données :**")
        for attr, ans in history:
            st.write("- " + question_from_attribute(attr) + " → " + label_from_value(attr, ans))

    if st.button("Recommencer"):
        st.session_state["node_id3"] = tree
        st.session_state["history_id3"] = []
        st.rerun()