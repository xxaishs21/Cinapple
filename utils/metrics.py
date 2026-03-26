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
    for i in range(len(a)):
        z = b[i] - a[i]
        d = d + z * z

    return math.sqrt(d)