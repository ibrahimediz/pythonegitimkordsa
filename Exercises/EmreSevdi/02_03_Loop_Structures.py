import random as rnd
for a in range(6):
    liste = []
    for i in range(6):
        sayi = rnd.randint(1,90)
        liste.append(sayi)
    print(*liste) 

