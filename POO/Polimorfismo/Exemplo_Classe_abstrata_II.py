'''
Segundo exemplo de Classe abstrata. Agora com método abstrato e ocorrendo
Herança e subsequentemente polimorsfismo.
'''

from abc import ABC, abstractmethod


class Pessoa(ABC):
    nome = None
    salario = 0

    @abstractmethod
    def calcular_salario(self, total):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome):
        self.nome = nome

    def calcular_salario(self, total):
        return self.salario * 1.2 + total


class Medico(Funcionario):
    def calcular_salario(self, total):
        return self.salario * 10


func = Funcionario('Lauro Mendes do Amaral Junior')
func.salario = 1000
print(f'Nome: {func.nome}\nSalário Atualizado: {func.calcular_salario(2568)}')
print()
print('TESTE: ')
medico = Medico('Dr Pamplona')
medico.salario = 50
print(f'Nome: {medico.nome}\nSalário Atualizado: {medico.calcular_salario(0)}')
