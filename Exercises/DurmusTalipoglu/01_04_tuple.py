import random
random.seed(2)
liste = [random.randint(1,100) for i in range(5)]

print(liste.sort(reverse=True))

print(liste)
print(liste[1])

liste.pop(1)
print(liste)

liste[0] = 1000
print(liste)

liste.insert(1, 250)
print(liste)
