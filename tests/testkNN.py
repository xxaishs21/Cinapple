from models.knn import kNN
from utils.loadmovies import loadmovies

Z = loadmovies()
print(kNN(Z, 3, Z[0]))