import random as rnd
liste = []
for i in range(6):
    liste.append(rnd.randint(1,49))
liste.sort()
print(*liste)