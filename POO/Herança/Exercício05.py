'''Exercício 05
Escreva um programa para armazenar dados de veículos.
Crie a classe Motor que contém cilindrada e potencia.
Crie a classe Veiculo contendo ano de fabricação, preco e motor. Crie também o
metodo exibir_dados para mostrar os dados do Veículo.
Crie a classe Carro, que herda da classe Veiculo e i nclua os atributos cor e
modelo. Crie também o metodo exibir_dados para mostrar os dados do Carro.
Crie a classe Caminhão, que herda da classe Veiculo e i nclua o atributos
comprimento (em metros). Crie também o metodo exibir_dados para mostrar os
dados do Caminhão.
'''


class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia


class Veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    def exibir_dados(self):
        print(f'[ Ano: {self.ano}\n  Preço: {self.preco}\n  Cilindrada:\
 {self.motor.cilindrada}\n  Potência: {self.motor.potencia}')


class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        print("Carro:")
        super().exibir_dados()
        print(f'  Cor: {self.cor}\n  Modelo {self.modelo} ]')
        print()


class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        print("Caminhão:")
        super().exibir_dados()
        print(f'  Comprimento: {self.comprimento} ]')
        print()


#  Utilize o programa abaixo para testar as classes
motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)
carro.exibir_dados() # imprime os valores de todos os atributos do carro
caminhao.exibir_dados() # imprime os valores de todos os atributos do caminhão
