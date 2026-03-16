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
    for movies in movies 
        new_movie = {}
        
        for feat in features : 
            new_movie[feat] = conv(movie[feat])

        new_movie["duration"] = conv_duration(movie["duration"])
        new_movie["family_friendly"] = conv_bool(movie["family_friendly"])
        new_movie["liked"] = conv_bool(movie["liked"])
        
        conv_movies.append(new_movie)
    
    return conv_movies
        
def entro_shannon(): 
    return 0

def gain_info(): 
    return 0


    