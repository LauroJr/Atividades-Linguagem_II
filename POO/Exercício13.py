'''Exercício 13

Implemente a classe CarroCorrida

|-------------------------|
|       CarroCorrida      |
|-------------------------|
|- numero: int            |
|- piloto: str            |
|- velocidade_axima: str  |
|- velocidade_atual: int  |
|- ligado: bool           |
|-------------------------|
|+ ligar()                |
|+ desligar()             |
|+ acelerar(velocidade)   |
|+ frear()                |
|-------------------------|


Classe CarroCorrida

Atributos (todos privados):
numero: número de identificação do carro
piloto: nome do piloto do carro ao carro
velocidade_maxima: velocidade máxima do carro em km/h
velocidade_atual: velocidade atual do carro em km/h (valor inicial deve ser
zero)
ligado: informa se o carro está ligado (valor inicial deve ser False)


Métodos:
ligar: define o carro como ligado
desligar: define o carro como desligado
acelerar: aumenta velocidade atual do carro em N km/h. O carro só pode
acelerar se estiver ligado. Ao acelerar, o carro nunca pode ultrapassar a sua
velocidade máxima
frear: define a velocidade atual do carro em 0 km/h.
Criar os métodos get e set, quando for necessário.
'''


class CarroCorrida:
    def __init__(self, prefixo, nome, vel_max):
        self.__numero = prefixo
        self.__piloto = nome
        self.__velocidade_maxima = vel_max
        self.__velocidade_atual = 0
        self.__ligado = False

    def ligar(self):
        if self.__ligado is False:
            self.__ligado = True

    def desligar(self):
        if self.__ligado is True and self.__velocidade_atual == 0:
            self.__ligado = False
            msg = "Carro desligado"
            return msg
        else:
            if self.__velocidade_atual > 0:
                msg = "Carro em movimento. Pare para desligar..."
                return msg
        if self.__ligado is False and self.__velocidade_atual == 0:
            msg = "Carro já consta desligado..."
            return msg

    def acelerar(self, velocidade):
        if self.__ligado is True:
            if self.__velocidade_atual + velocidade > 150:
                self.__velocidade_atual = 150
                print("Não ultrapassar velocidade max...")
            else:
                self.__velocidade_atual += velocidade

    def frear(self):
        self.__velocidade_atual = 0

    def get_velocidade_atual(self):
        return self.__velocidade_atual


carro = CarroCorrida(1, "Lauro Jr", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())  # imprime 0, porque o carro está desligado
carro.ligar()
carro.acelerar(20)
print(carro.get_velocidade_atual())  # imprime 20
print(carro.desligar())
carro.acelerar(80)
print(carro.get_velocidade_atual())  # imprime 100
carro.acelerar(70)
print(carro.get_velocidade_atual())  # imprime 150, não ultrapassar a vel. max.
carro.frear()
print(carro.get_velocidade_atual())  # imprime 0 '''
print(carro.desligar())
print(carro.desligar())
