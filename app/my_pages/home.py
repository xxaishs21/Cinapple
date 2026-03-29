import streamlit as st

def render():
    st.title("🎬 Cinapple 🎬")
    st.subheader("Une application d'analyse et de recommandation de films")

    st.write(
        """
        Bienvenue sur **Cinapple** ! 
        
        Cette application permet d'explorer une base de films à l'aide de plusieurs algoriths d'apprentissage automotatique. 
        
        L'objectif est de : 
        - prédire si un film peut etre aimé ou non ; 
        - guider le choix d'un film selon les envies ; 
        - regrouper des films selon leur ressemblance. 
        """
    )

    st.markdown("---")

    st.header("Algorithmes utilisés")

    st.write(
        """
        **k plus proches voisins (k-NN)** : 
        \nPrévoit si un film peut plaire à partir des films les plus proches.
        """
    )

    st.write(
        """
        **ID3** : 
        \nConstruit un arbre de decision pour oreinter l'utilisateur dans le choix d'un film.
        """
    )

    st.write(
        """
        **k-moyennes** : 
        \nRegroupe automatiquement les films en plusieurs catégories selons leurs caractéristiques.
        """
    )

    st.markdown("---")

    st.header("A propos du projet")

    st.write(
        """
        Ce projet a été concu pour comparer plusieurs approches d'apprentissage supervisé et non supervisé sur une meme base de films. 
        
        Il sert à la fois d'outils de recommandation et de support pédagogique pour mieux comprendre le fonctionnement des algorithmes. 
        """
    )
