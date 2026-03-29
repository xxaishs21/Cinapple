import math 

features = [
    "action",
    "humor",
    "romance",
    "emotion",
    "intensity",
    "duration",
    "family_friendly",
    "dark"
]

def distance(a, b):
    """
    Calcule la distance euclidienne normalisée entre deux vecteurs représentant des films.
    Chaque film est décrit par un ensemble de caractéristiques numériques
    (action, humour, romance, émotion, intensité, durée, familial, sombre).

    La fonction :
    - convertit les entrées en listes,
    - normalise chaque caractéristique pour éviter qu’une variable (comme la durée)
      domine le calcul,
    - calcule la distance euclidienne entre les deux vecteurs.

    Paramètres :
    a : liste ou structure itérable
        Vecteur du premier film.
    b : liste ou structure itérable
        Vecteur du second film.

    Retour :
    float
        Distance entre les deux films (plus elle est petite, plus les films sont similaires).
    """   
    a = list(a)
    b = list(b)
    ranges = [10, 10, 10, 10, 10, 200, 1, 1]

    d = 0
    for i in range(len(a)):
        z = (b[i] - a[i]) / ranges[i]
        d += z * z
    return math.sqrt(d)