'''Exercício 06
Uma universidade necessita de um sistema que facilite a sua gestão acadêmica.
Implemente as classes de modo que obedeçam os relacionamentos apresentados no
diagrama abaixo:
Sabe-se que um professor é um funcionário. Além de professores, há
funcionários que são técnicos administrativos.
Para cada funcionário, i ndependente de ser professor ou técnico, é necessário
saber seu nome, endereço, telefone, cpf e salário.
Especificamente para professores, é necessário saber sua titulação e as
disciplinas que ele leciona. Especificamente para técnicos administrativos, é
necessário saber seu cargo.
Para cada aluno é necessário saber seu nome, endereco, telefone, cpf e as
disciplinas que ele cursa.
Para cada disciplina é necessário registrar seu nome.
'''


class Pessoa:
    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf


class Aluno(Pessoa):
    def __init__(self, nome, endereco, fone, cpf):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = []

    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)


class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria


class Funcionario(Pessoa):
    def __init__(self, nome, endereco, fone, cpf, salario):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario


class Professor(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, titulacao):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.titulacao = titulacao
        self.disciplina = []

    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)


class Tecnico(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.cargo = cargo


aluno1 = Aluno('Lauro Jr', 'Rua João Mateus/ 145a', '(11)96187-0730', '408.850.168-31')
disciplina1_aluno1 = Disciplina('DevOps', '60 hrs')
disciplina2_aluno1 = Disciplina('Git e Github', '15 hrs')
aluno1.incluir_disciplina(disciplina1_aluno1)
aluno1.incluir_disciplina(disciplina2_aluno1)

print("Dados do Aluno1:")
print(aluno1.nome)
print(aluno1.endereco)
print(aluno1.fone)
print(aluno1.cpf)
for disc in aluno1.disciplina:
    print(disc.nome)

professor1 = Professor('Daniel Jr', 'Rua João Mateus/ 145a', '(11)2011-2088', '985.580.658-65', 2500.25, 'Professor')
disciplina1_professor1 = Disciplina('Eng/ Software', '80 hrs')
disciplina2_professor1 = Disciplina('SQL/ BD', '80')
professor1.incluir_disciplina(disciplina1_professor1)
professor1.incluir_disciplina(disciplina2_professor1)

print()
print("Dados do Professor:")
print(professor1.nome)
print(professor1.endereco)
print(professor1.fone)
print(professor1.cpf)
print(professor1.salario)
for disc in professor1.disciplina:
    print(disc.nome)
print()

tecnico1 = Tecnico('João Dias', 'Rua Japão/ 25b', '(11)2954-3565', '568.565.235-21', 1855.65, 'Eletricista')
print("Dados do tecnico:")
print(tecnico1.nome)
print(tecnico1.endereco)
print(tecnico1.fone)
print(tecnico1.cpf)
print(tecnico1.salario)
print(tecnico1.cargo)
