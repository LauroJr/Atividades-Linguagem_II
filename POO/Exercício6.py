'''Exercício 06

A associação entre classes ocorre quando uma classe possui atributos que são
objetos de outra classe.

Implemente as classes Pessoa e Carro.

Classe Pessoa:
Atributos:
nome: nome da pessoa (valor inicial definido no construtor)
idade: idade da pessoa (valor inicial definido no construtor)
carro: objeto da classe Carro (valor inicial None)
Métodos:
comprar_carro: recebe um objeto Carro e associa esse objeto ao atributo carro.

Classe Carro:
Atributos:
marca: marca do carro (valor inicial definido no construtor)
modelo: modelo do carro (valor inicial definido no construtor)
placa: placa do carro (valor inicial definido no construtor)
ano: ano de fabricação do carro (valor inicial definido no construtor)
Métodos:
Não possui
'''


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, my_car):
        self.carro = my_car
        return


class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)                     # imprime João
print('Modelo do meu carro: ', eu.carro.modelo)  # imprime Gol
print('Placa do meu carro: ', eu.carro.placa)    # imprime AAA-1111
