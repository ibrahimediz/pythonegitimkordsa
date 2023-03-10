import random as rnd
for y in range(6):
    liste = []
    for i in range(6):
        sayi = rnd.randint(1,49)
        while sayi in liste:
            sayi = rnd.randint(1,49)
        liste.append(sayi)
    liste.sort()
    print(*liste)