lista = []
arquivo_pares = open("pares.txt", "r")
arquivo_impares = open("impares.txt", "r")

for num in arquivo_pares:
    lista.append(int(num))

for num in arquivo_impares:
    lista.append(int(num))

lista.sort()
print(lista)

novo_arquivo = open('numeros_ordenados.txt', 'w')

for i in lista:
    novo_arquivo.write(str(i) + '\n')

arquivo_pares.close()
arquivo_impares.close()
