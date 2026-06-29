# Cinapple

Cinapple est une application de recommandation de films qui analyse les goûts d’un utilisateur à partir de plusieurs caractéristiques. Elle permet de prédire si un film peut lui plaire, de guider le choix d’un film à partir de réponses à des questions, et de regrouper les films selon leurs ressemblances grâce à plusieurs algorithmes d’apprentissage automatique.

Ce projet a été conçu pour comparer plusieurs approches d’apprentissage supervisé et non supervisé sur une même base de films. Il sert à la fois d’outil de recommandation et de support pédagogique pour mieux comprendre le fonctionnement des algorithmes.

## Objectif

Ce projet a pour objectif de :

- permettre la création d’une base de données personnalisée ;
- prédire si un film peut être aimé ou non ;
- guider le choix d’un film selon les envies de l’utilisateur ;
- regrouper des films selon leurs ressemblances.

L’utilisateur peut également vivre une expérience personnalisée. Avant d’utiliser les algorithmes, il peut noter certains films dans l’onglet **Base personnalisée**. Plus les films sont notés, plus les recommandations deviennent pertinentes.

## Algorithmes utilisés

### k plus proches voisins (k-NN)
Prévoit si un film peut plaire ou non à l’utilisateur en fonction des films les plus proches présents dans la base de données.

### ID3
Construit un arbre de décision en posant des questions à l’utilisateur afin de l’orienter dans le choix d’un film présent dans la base de données.

### k-moyennes
Regroupe automatiquement les films de la base de données en `k` catégories, choisies par l’utilisateur, selon leurs caractéristiques.

## Interface

L’application a été réalisée avec **Streamlit** et organisée en plusieurs pages :

- **Accueil**
- **Recommandation k-NN**
- **Conseiller ID3**
- **Groupes de films**
- **Base personnalisée**

## Installation

Clone le projet puis installe les dépendances nécessaires.

```bash
pip install -r requirements.txt
