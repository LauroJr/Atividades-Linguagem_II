'''Exercício 03 - Classe Funcionário

Implemente uma classe Funcionario.
Atributos:
 - nome
 - salario
Métodos:
 - aumentar_salario: recebe como parâmetro de entrada um percentual e
altera o salário do funcionário, de acordo com o percentual recebido.

Crie um programa que utilize esta classe. Ele deve pedir ao usuário
o nome e o salário do funcionário e criar um objeto. Depois, deve
solicitar ao usuário o percentual de aumento e executar o método
aumentar salário. Na sequência deve imprimir o salário do
funcionário atualizado.
'''


class Funcionario():

    def __init__(self, nome, salar):
        self.nome = nome
        self.salario = salar

    def aumentar_salario(self, porcentual):
        total = (self.salario * porcentual) / 100 + self.salario
        print("Nome: ", self.nome)
        print("Salário atual: ", self.salario)
        print("Novo salário: ", total)


nome = input("Nome: ")
salar = float(input("Salário: "))
porcentual = float(input("Quantos porcentos deseja aumentar o salário: "))

fun = Funcionario(nome, salar)
fun.aumentar_salario(porcentual)
