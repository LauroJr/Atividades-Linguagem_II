'''
Exercício 03
Crie uma estrutura hierárquica que contenha as seguintes classes:
Veiculo (classe abstrata)
Bicicleta
Automovel

Os métodos da classe Veiculo são todos e abstratos e devem ser implementados
nas classes filhas: limpar - imprime a mensagem “Bicicleta/Automóvel foi limpo”
consertar - imprime a mensagem “Bicicleta/Automóvel foi consertado”

Acrescentar na classe Automovel o método:
trocar_oleo - imprime a mensagem “O óleo foi trocado”
Ao consertar o carro, deve ser exibida também a mensagem de que o óleo foi
trocado.
OBS.: As classes não possuem atributos.
'''
from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def limpar(self):
        pass

    @abstractmethod
    def consertar(self):
        pass


class Bicicleta(Veiculo):

    def limpar(self):
        print('Bicicleta foi limpa!')

    def consertar(self):
        print('Bicicleta foi consertada')


class Automovel(Veiculo):

    def limpar(self):
        print('Automóvel foi limpo')

    def consertar(self):
        print('Automóvel foi consertado\nÓleo trocado com sucesso')

    def trocar_oleo(self):
        print('O óleo foi trocado')


bike = Bicicleta()
carro = Automovel()

bike.limpar()
bike.consertar()
print()

carro.limpar()
carro.consertar()
carro.trocar_oleo()
