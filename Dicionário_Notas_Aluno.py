def calcula_media(x):
    media = []
    a = []
    for I in x:
        total = sum(x[I])/2
        a.append(total)
    return a


Media_Aluno = {}
lista_Notas = []
c = 0

while c < 3:
    nome_aluno = input("Nome do Aluno: ")
    for I in range(2):
        nota_aluno = float(input("Nota de: "))
        lista_Notas.append(nota_aluno)
    c = c + 1
    Media_Aluno[nome_aluno] = lista_Notas
    lista_Notas = []

print(Media_Aluno)

Result = calcula_media(Media_Aluno)
print(Result)
