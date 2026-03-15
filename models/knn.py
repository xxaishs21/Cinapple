from utils.metrics import distance

def kNN(Z, k, x) : 
    assert(k <= len(Z))
    
    distances = []
    for y in Z :
        distances.append([distance(x, y), y["title"], y["liked"]])
    distances.sort()
    
    classe_yes = 0
    classe_no = 0
    for i in range(k) : 
        if distances[i][2] == 1 :
            classe_yes += 1
        else : 
            classe_no += 1
    
    if classe_yes >= classe_no : 
        return 1
    else : 
        return 0
    
