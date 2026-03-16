import math

from utils.loadmovies import loadmovies 



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

def conv(el) : 
    if el > 7 : 
        return "fort"
    elif el < 4 : 
        return "faible"
    else : 
        return "moyen"

def conv_duration(d) : 
    if d < 100:
        return "court"
    elif d <= 140 : 
        return "moyen"
    else : 
        return "long"

def conv_bool(v) : 
    if v == 1 : 
        return "oui" 
    else : 
        return "non"

def conv_class_id3() : 
    movies = loadmovies() 
    conv_movies = []
    for movie in movies :
        new_movie = {}
        
        for feat in features : 
            new_movie[feat] = conv(movie[feat])

        new_movie["duration"] = conv_duration(movie["duration"])
        new_movie["family_friendly"] = conv_bool(movie["family_friendly"])
        new_movie["liked"] = movie["liked"]
        
        conv_movies.append(new_movie)
    
    return conv_movies
        
def entro_shannon(S): 
    like = 0 
    no_like = 0
    h = 0 
    
    if S == [] : 
        return 0
    
    else : 
        for movie in S : 
            like = like + movie["liked"]
        no_like = len(S) - like 

        if like == 0 or no_like == 0 : 
            return 0
        
        h = h - ((like/len(S)) * math.log2(like/len(S))) - ((no_like/len(S)) * math.log2(no_like/len(S)))
    
    return h     


def gain_info(S, a): 
    s = 0
    ssens =  {}

    
    if S == [] : 
        return 0
        

    for movie in S : 
        val = movie[a]
        if val not in ssens : 
            ssens[val] = []
        ssens[val].append(movie)
    
    for val in ssens: 
        sv = ssens[val]
        s = s + (len(sv) / len(S)) * entro_shannon(sv)
        
    return entro_shannon(S) - s

def mm_class(S) :   
    c = S[0]["liked"]
    for movie in S : 
        if movie["liked"] != c : 
            return False 
    return True #traite aussi le cas où S est vide

def maj_class(S) : 
    like = 0
    no_like = 0 
    
    for movie in S : 
        if movie["liked"] == 1 : 
            like += 1
        else : 
            no_like += 1
    
    if like >= no_like : 
        return 1 
    else : 
        return false 

def best_att(S, A) : 
    battr = A[0]
    bgain = gain_info(S, A[0])
    
    for a in A : 
        g = gain_info(S, a)
        if g > bgain : 
            bgain = g 
            battr = a 
    
    return battr

def id3(S, A): 
    if 
    
    tree = {
        "type" : "noeud",
        "attribut": a, 
        "enfants": {}
    }