from utils.metrics import distance

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

def transfo_en_vecteur(film):
    vect = []
    for i in features:
        vect.append(film[i])
    return vect

def centre_plus_proche(film, centres):
    v = transfo_en_vecteur(film)
    best_dist = distance(v, centres[0])
    best_i = 0

    for i in range(len(centres)):
        d = distance(v, centres[i])
        if d < best_dist:
            best_dist = d
            best_i = i

    return best_i

def cluster(films, centres):
    clus = []
    for i in range(len(centres)):
        clus.append([])

    for f in films:
        clus[centre_plus_proche(f, centres)].append(f)

    return clus

def calcul_centre(clus):
    if clus == []:
        return None

    n = len(features)
    centre = [0] * n

    for f in clus:
        vect = transfo_en_vecteur(f)
        for i in range(n):
            centre[i] += vect[i]

    for i in range(n):
        centre[i] = centre[i] / len(clus)

    return centre

def nv_centres(clus, anciens_centres):
    centres = []
    for i in range(len(clus)):
        if clus[i] == []:
            centres.append(anciens_centres[i])
        else:
            centres.append(calcul_centre(clus[i]))
    return centres

def k_moyennes(f, k, max_iter=100):
    c = []
    for i in range(k):
        c.append(transfo_en_vecteur(f[i]))

    for _ in range(max_iter):
        clus = cluster(f, c)
        nv = nv_centres(clus, c)

        if nv == c:
            return c, clus

        c = nv

    return c, clus