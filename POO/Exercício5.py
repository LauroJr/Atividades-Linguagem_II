'''Exercício 05 - Classe Carro

Implemente uma classe Carro

Propriedades:
 - consumo (medidos em km/litro): O consumo deve ser especificado no
construtor.
 - quantidade_combustivel (quantidade de litros de combustível no
tanque do carro): a quantidade inicial deve ser zero

Métodos:
 - adicionar_combustivel: recebe uma quantidade de litros de
combustível para abastecer o tanque.
 - obter_combustivel: retorna a quantidade atual de combustível.
 - andar: recebe uma distância em km e simula o ato de dirigir o
veículo por essa distância, reduzindo o nível de combustível no
tanque de gasolina (de acordo com o consumo do veículo)
'''


class Carro:

    def __init__(self, km_lt):
        self.consumo = km_lt
        self.quantidade_combustivel = 0

    def adicionar_combustivel(self, tanque):
        self.quantidade_combustivel = self.quantidade_combustivel + tanque

    def obter_combustivel(self, a):
        return self.quantidade_combustivel

    def andar(self, km_andar):
        self.quantidade_combustivel = self.quantidade_combustivel - (km_andar / self.consumo)


fusca = Carro(15)  # 15 quilômetros por litro de combustível

fusca.adicionar_combustivel(20)  # abastece com 20 litros de combustível

fusca.andar(100)  # anda 100 quilômetros.

print(fusca.obter_combustivel(fusca.quantidade_combustivel))
# imprime o combustível que resta no tanque
