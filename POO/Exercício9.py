''' Exercício 04

Classe Emprego

    Atributos:
        cargo:
        salario:
        bonus: percentual de bonificação a ser acrescentado ao salário do
        funcionário, de acordo com a quantidade de dependentes. Por exemplo,
        se o bônus for de 2%, e o funcionário tiver 3 dependentes, ele
        receberá 6% de acréscimo sobre o salário.
    Métodos:
        não possui


Classe Pessoa
    Atributos:
        nome
        fone
        email
        emprego: objeto do tipo Emprego
        dependentes: lista de objetos do tipo Pessoa
    Métodos:
        calcular_salario: retorna o valor do salário do funcionário, de acordo
        com o percentual de bonificação e quantidade de dependentes.
'''


class Pessoa:

    def __init__(self, nome, cel, email, objeto1, n_dpe):
        self.nome = nome
        self.fone = cel
        self.email = email
        self.emprego = objeto1
        self.dependentes = n_dpe

    def calcular_salario(self):
        sal_atual = (self.dependentes * objeto2.emprego.bonus *
                     objeto2.emprego.salario) / 100 + objeto2.emprego.salario
        return sal_atual


class Emprego:

    def __init__(self, cargo, salario, bonus):
        self.cargo = cargo
        self.salario = salario
        self.bonus = bonus


objeto1 = Emprego('Desenvolvedor', 1955.58, 3)
objeto2 = Pessoa('Lauro', '(11)96187-0730', 'lauro@gmail.com', objeto1, 3)
a = objeto2.calcular_salario()
print(a)
