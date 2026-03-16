import math 

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

def distance(a, b):
    d = 0
    for feature in features:
        z = b[feature] - a[feature]
        d = d + z * z

    return math.sqrt(d)