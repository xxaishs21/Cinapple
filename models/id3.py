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

def conv_class_id3(f) : 
    movies = loadmovies(f) 
    conv_movies = []
    for movies in movies :
        new_movie = {}
        
        for feat in features : 
            new_movie[feat] = conv(movie[feat])

        new_movie["duration"] = conv_duration(movie["duration"])
        new_movie["family_friendly"] = conv_bool(movie["family_friendly"])
        new_movie["liked"] = conv_bool(movie["liked"])
        
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


def gain_info(): 
    return 0


    