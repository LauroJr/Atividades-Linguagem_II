from occupation import soma 

lista = []
c = 0

while c <= 5:
    a = int(input("Digite um valor: "))
    lista.append(a)
    c = c+1

Resultado = soma(lista)
print(Resultado)
