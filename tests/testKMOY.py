from utils.loadmovies import loadmovies
from models.kmoy import k_moyennes

films = loadmovies()
centres, clus = k_moyennes(films, 3)

print("Nombre de centres :", len(centres))
for i in range(len(clus)):
    print("Cluster", i, ":", len(clus[i]), "films")
    for film in clus[i]:
        print(" -", film["title"])
    print()