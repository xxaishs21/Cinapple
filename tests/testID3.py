from models.id3 import *

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