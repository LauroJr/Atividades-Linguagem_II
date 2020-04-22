import os
import time

'''Exercício 01

Implemente a classe Filme, conforme o diagrama de classes abaixo
Todos os atributos devem ser privados
Crie os métodos get e set para todos os atributos

|-----------------------|
|        Filme          |
|-----------------------|
|- titulo: str          |
|- genero: str          |
|-----------------------|
| + get_titulo()        |
| + get_genero()        |
| + set_titulo(titulo)  |
| + set_genero(genero)  |
|-----------------------|


No seu programa principal, faça a seguinte implementação:
Criar uma lista de filmes vazia
Cadastrar 3 filmes (com os dados informados pelo usuário)
Armazenar os dados de cada filme em um objeto da classe Filme
Armazenar os objetos na lista de filmes
Exibir um relatório com os dados de todos os filmes cadastrados
'''


class Filme:
    def __init__(self):
        self.__titulo = None
        self.__genero = None

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


lista_filmes = []
cont = 0

for filme in range(3):
    cont += 1
    filme = Filme()
    titulo = input(f'Cadastre o nome do {cont}º filme: ')
    genero = input(f'Qual o gênero do filme {titulo} ?: ')
    print()
    filme.set_titulo(titulo)
    filme.set_genero(genero)
    lista_filmes.append(filme)
print()
cont = 0

for i in range(101):
    print("Computando...")
    print(f"{i}%")
    print(i*'◼')
    time.sleep(0.03)
    os.system("cls")

for filme in lista_filmes:
    cont += 1
    print(f'{cont}º filme : {filme.get_titulo()}')
    print(f'gênero do {cont}º filme: {filme.get_genero()}')
    print()
