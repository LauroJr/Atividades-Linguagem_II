from random import randint


lista1 = []
for I in range(1,11):
    lista1.append(randint(1, 6))

print(lista1) 

for I in range(1, 7):
    n = lista1.count(I)
    if n > 1:
        print("O número ",I," aparece ",n," vezes.")
    if n == 1:
        print("O número ",I," aparece ",n," vez.")
