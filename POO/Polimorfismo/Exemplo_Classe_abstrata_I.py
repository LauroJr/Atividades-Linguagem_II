'''
Primeiro exemplo de Classe abstrata, com atributos, e método abstrato.
'''

from abc import ABC, abstractmethod


class Pessoa(ABC):
    nome = None
    salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass
