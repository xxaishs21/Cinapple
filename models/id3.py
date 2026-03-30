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

def conv_class_id3():
    movies = loadmovies()
    conv_movies = []

    for movie in movies:
        new_movie = {}

        new_movie["title"] = movie["title"]
        new_movie["action"] = conv(movie["action"])
        new_movie["humor"] = conv(movie["humor"])
        new_movie["romance"] = conv(movie["romance"])
        new_movie["emotion"] = conv(movie["emotion"])
        new_movie["intensity"] = conv(movie["intensity"])
        new_movie["duration"] = conv_duration(movie["duration"])
        new_movie["family_friendly"] = conv_bool(movie["family_friendly"])
        new_movie["dark"] = conv(movie["dark"])
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
        return 0 

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
    if S == [] : 
        return {"type" : "leaf", "class": 0}
    
    if mm_class(S) : 
        return {"type" : "leaf", "class": S[0]["liked"]}
    
    if A == [] : 
        return{"type": "leaf", "class": maj_class(S)}
    
    a = best_att(S, A)
    
    tree = {
        "type" : "node",
        "attribute": a, 
        "children": {}
    }
    
    val = []
    for movie in S : 
        if movie[a] not in val : 
            val.append(movie[a])
    
    newA = []
    for attr in A : 
        if attr != a : 
            newA.append(attr)
    
    for v in val : 
        Sv = []
        for movie in S: 
            if movie[a] == v: 
                Sv.append(movie)
        
        tree["children"][v] = id3(Sv, newA)
    
    return tree

def print_tree(tree, indent=""):
    if tree["type"] == "leaf":
        if tree["class"] == 1:
            print(indent + "-> aimé")
        else:
            print(indent + "-> pas aimé")
        return

    print(indent + "[" + tree["attribute"] + "]")

    for value, child in tree["children"].items():
        print(indent + "  " + str(value) + " :")
        print_tree(child, indent + "    ")

def predict_id3(tree, movie): 
    if tree["type"] == "leaf" : 
        return tree["class"]
    
    value = movie[tree["attribute"]]
    
    if value not in tree["children"] : 
        return None 
    
    return predict_id3(tree["children"][value], movie)

def affiche_classe(c):
    if c == 1 : 
        return "aimé"
    elif c == 0 : 
        return "pas aimé"
    else : 
        return "inconnu"
