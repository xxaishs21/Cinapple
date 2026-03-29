from utils.metrics import distance

def kNN(Z, k, x) : 
    assert(k <= len(Z))
    
    distances = []
    for y in Z :
        distances.append([distance(x, y["vect"]), y["title"], y["liked"]])
    distances.sort()
    
    classe_yes = 0
    classe_no = 0
    for i in range(k) : 
        dist = distances[i][0]
        if distances[i][2] == 1:
            classe_yes += 1 / (dist + 0.0001)
        else:
            classe_no += 1 / (dist + 0.0001)
            
    # moyenne des distances des k voisins
    return (sum(d[0] for d in distances[:k]) / k)
