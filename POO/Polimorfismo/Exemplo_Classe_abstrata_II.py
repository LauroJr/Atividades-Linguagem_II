'''
Segundo exemplo de Classe abstrata. Agora com método abstrato e ocorrendo
Herança e subsequentemente polimorsfismo.
'''

from abc import ABC, abstractmethod


class Pessoa(ABC):
    nome = None
    salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome):
        self.nome = nome

    def calcular_salario(self):
        return self.salario * 1.2


func = Funcionario('Lauro Mendes do Amaral Junior')
func.salario = 1000
print(f'Nome: {func.nome}\nSalário Atualizado: {func.calcular_salario()}')
