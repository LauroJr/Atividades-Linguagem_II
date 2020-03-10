lista1 = [0]*10
c = 0
lista2 = []

for I in lista1:
    n = int(input("Digite um número: "))
    lista1[c] = n
    c = c + 1
# print(lista1)

Maior_Num = max(lista1)
Menor_Num = min(lista1)
Media_Num = (sum(lista1)/10)
for I in lista1:
    if I < Media_Num:
        lista2.append(I)


print("")
print("Segue MAIOR - MENOR - MEDIA dos números digitados: ")
print("")
print(Maior_Num)
print(Menor_Num)
print(Media_Num)
print("Lista com números maiores que a média: ",lista2)
