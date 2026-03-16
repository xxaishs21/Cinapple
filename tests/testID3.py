from models.id3 import *

S1 = [{"liked": 1}, {"liked": 1}, {"liked": 1}]
S2 = [{"liked": 1}, {"liked": 0}]
S3 = [{"liked": 1}, {"liked": 1}, {"liked": 1}, {"liked": 0}]

print(entro_shannon(S1))
print(entro_shannon(S2))
print(entro_shannon(S3))
