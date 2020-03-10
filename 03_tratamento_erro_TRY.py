'''Crie uma lista, inicialmente vazia, para armazenar uma listagem de nomes.
a) Criar uma função para inserir um nome na lista

b) Criar uma função que recebe como parâmetro a lista e uma posição (índice)
dessa lista e retornar o nome que está nessa posição. Essa função deve gerar
e tratar uma exceção do tipo IndexError caso o índice não exista na lista.
'''


def inserir_nome(a):
    lista.append(input())
    nome = lista
    return nome


def mostrar_nome(a, b):
    try:
        print(a[b])
    except IndexError:
        print("Indice inexistente")
        print("Tente novamente ou saia do programa")


lista = []
continuar = True
while continuar:
    print("""
    [1] INSERIR NOME
    [2] ESCOLHA QUAL INDICE QUER ACESSAR
    [3] SAIR """)
    a = int(input())
    if a == 1:
        nome = inserir_nome(lista)
        continuar = True
    elif a == 2:
        ind = int(input("Qual indice quer acessar: "))
        mostrar_nome(nome, ind)
        continuar = True
    else:
        continuar = False

mostrar = int(input("Tecle 1 para mostrar a lista: "))
if mostrar == 1:
    print(lista)
