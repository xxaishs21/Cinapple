from models.id3 import *

"""
S1 = [{"liked": 1}, {"liked": 1}, {"liked": 1}]
S2 = [{"liked": 1}, {"liked": 0}]
S3 = [{"liked": 1}, {"liked": 1}, {"liked": 1}, {"liked": 0}]
print(entro_shannon(S1))
print(entro_shannon(S2))
print(entro_shannon(S3))

movies_id3 = conv_class_id3()
print(gain_info(movies_id3, "action"))
print(gain_info(movies_id3, "duration"))
print(gain_info(movies_id3, "family_friendly"))

movies_id3 = conv_class_id3()
A = [
    "action",
    "humor",
    "romance",
    "emotion",
    "intensity",
    "duration",
    "family_friendly",
    "dark"
]
tree = id3(movies_id3, A)
print_tree(tree)
"""

movies_id3 = conv_class_id3()
tree = id3(movies_id3, features)

print_tree(tree)

x = movies_id3[0]
print("Film testé :", x)
print("Classe réelle :", affiche_classe(x["liked"]))
print("Classe prédite :", affiche_classe(predict_id3(tree, x)))