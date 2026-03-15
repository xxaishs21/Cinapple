import math 

def distance(a, b):
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

    d = 0
    for feature in features:
        z = b[feature] - a[feature]
        d = d + z * z

    return math.sqrt(d)