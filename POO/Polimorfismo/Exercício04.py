'''
Exercício 04
Crie uma hierarquia de classes para representar os diferentes tipos de funcionários de um escritório
que tem os seguintes cargos: gerente, assistente e vendedor.
Escreva uma classe base abstrata chamada Funcionario que declara um método abstrato
calcular_salario()
Essa classe também deve definir os seguintes atributos: nome , matricula e salario_base .
Essa classe abstrata deverá ser herdada pelas outras classes que são: Gerente, Assistente e
Vendedor .
Em cada classe filha deve-se sobrescrever o método calcular_salario(). Este método deve calcular
e retornar o salário de cada funcionário, da seguinte forma:
- O gerente recebe duas vezes o salário_base.
- O assistente recebe o salário_base.
- O vendedor recebe o salário_base mais uma comissão de 10%.
Implemente um programa principal que cria um objeto de cada tipo (gerente, assistente e vendedor)
e os armazena em uma lista
Percorra essa lista e imprima o salário de cada funcionário.
'''

from abc import ABC, abstractmethod


class Funcionario(ABC):
    nome = None
    matricula = None
    salario_base = 1300.00

    @abstractmethod
    def calcular_salario(self, salario):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def calcular_salario(self):
        return self.salario_base * 10 / 100 + self.salario_base


gerente = Gerente('Lauro Jr', '154825')
assistente = Assistente('Mônica Albuquerque', '132649')
vendedor = Vendedor('Alisson Moaraes', '132648')

lista_func = [gerente, assistente, vendedor]

for func in lista_func:
    print(f'Nome: {func.nome}\nSalário: {func.calcular_salario()}')
    print()
