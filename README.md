# Cinapple
Cinapple est une application de recommandation de films qui analyse les goûts d’un utilisateur à partir de plusieurs caractéristiques. Elle permet de prédire si un film peut lui plaire, de trouver un film à partir de réponses à des questions et de regrouper les films selon leurs ressemblances grâce à plusieurs algorithmes d’apprentissage automatique.
Ce projet a été concu pour comparer plusieurs approches d'apprentissage supervisé et non supervisé sur une meme base de films. Il sert à la fois d'outils de recommandation et de support pédagogique pour mieux comprendre le fonctionnement des algorithmes.

## Objectif 
Je me propose de : 
- permettre de faire une base de donnée personnalisé ; 
- prédire si un film peut etre aimé ou non ;
- guider le choix d'un film selon les envies ;
- regrouper des films selon leur ressemblance.

L'utilisateur peut également faire une expérience personnalisée. Avant d'utiliser les algorithmes, il faut donner une note à certains films dans l'onglet "Base personnalisée". Plus les films sont notés, plus les recommandations seront précises.


## Algorithmes utilisés 
- k plus proches voisins (k-NN) :

Prévoit si un film peut plaire ou non à l'utilisateur en fonction des films les plus proches qui sont présents dans la base de données.

- ID3 :

Construit un arbre de decision en posant des questions à l'utilisateur l'orienter dans le choix d'un film présent dans la base de donnée.

- k-moyennes :

Regroupe automatiquement les films de la base de données en k catégories, choix laissé à l'utilisateur, selons leurs caractéristiques.


## Bibliographie commentée 
Cette bibliographie rassemble quelques ressources de référence utilisées pour appuyer la conception de l’application Cinapple. Les algorithmes ont été réimplémentés en Python dans le projet, mais ces documents ont servi à vérifier les principes théoriques, les usages classiques et certaines limites des méthodes employées.

Les documentations de scikit-learn sur les plus proches voisins ont servi de point d’appui pour la partie recommandation. Elles rappellent que les méthodes de type k-NN reposent sur le calcul d’une distance entre un point à prédire et des exemples déjà connus, puis sur un vote des voisins les plus proches. Elles insistent aussi sur le rôle du paramètre `k` et sur l’importance du choix de la métrique, ce qui justifie directement les choix réalisés dans le projet pour la comparaison entre films à partir de leurs caractéristiques numériques. [1]

Pour la partie arbre de décision, les ressources de scikit-learn consacrées aux arbres et au critère `entropy` ont apporté un cadre théorique clair. Elles permettent de relier l’implémentation de l’algorithme ID3 à des notions centrales comme l’entropie de Shannon, le gain d’information et la construction récursive de règles de décision simples. Elles ont surtout été utiles pour justifier la logique générale du conseiller : poser des questions successives, réduire l’incertitude, puis aboutir à une décision finale. [2]

La partie consacrée au regroupement automatique des films s’appuie sur les ressources de scikit-learn relatives au clustering et à l’algorithme k-means. Elles décrivent le principe du partitionnement en groupes autour de centroïdes, ainsi que l’objectif d’inertie minimisée à l’intérieur des clusters. Elles rappellent également que l’algorithme est rapide en pratique mais sensible aux minima locaux, ce qui éclaire les choix faits dans le projet concernant l’initialisation des centres et les itérations successives jusqu’à stabilisation. [3]

La mise en forme de l’application s’appuie enfin sur la documentation officielle de Streamlit. Celle-ci présente à la fois la création d’applications multipages et les différentes façons d’organiser la navigation entre plusieurs vues. Ces ressources ont été particulièrement utiles pour structurer Cinapple en plusieurs pages distinctes — accueil, recommandation, conseiller, regroupement — tout en conservant une interface simple et lisible. [4]

### Références

- [1] **scikit-learn** — *Nearest Neighbors* : https://scikit-learn.org/stable/modules/neighbors.html
- [2] **scikit-learn** — *KNeighborsClassifier* : https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
- [3] **scikit-learn** — *Decision Trees* : https://scikit-learn.org/stable/modules/tree.html
- [4] **scikit-learn** — *DecisionTreeClassifier* : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
- [5] **scikit-learn** — *Understanding the decision tree structure* : https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html
- [6] **scikit-learn** — *Clustering* : https://scikit-learn.org/stable/modules/clustering.html
- [7] **scikit-learn** — *KMeans* : https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
- [8] **Streamlit Docs** — *Create a multipage app* : https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
- [9] **Streamlit Docs** — *Overview of multipage apps* : https://docs.streamlit.io/develop/concepts/multipage-apps/overview
- [10] **Streamlit Docs** — *Creating multipage apps using the `pages/` directory* : https://docs.streamlit.io/develop/concepts/multipage-apps/pages-directory