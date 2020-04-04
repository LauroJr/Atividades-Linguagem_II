''' Exercício 05

Logo abaixo encontramos um relacionamento apartir de 3 classes.
Temos uma classe Exame, outra Medico, e uma ultima Paciente. Iremos relacionar
Paciente e Medico com Exames, para imprimir o resultado, com ambos resultados

Deve exibir relatório com todos os dados do exame (inclusive os dados
do médico e paciente).
'''


class Exame:

    def __init__(self, objeto_medico, objeto_paciente, descr, result):
        self.medico = objeto_medico
        self.paciente = objeto_paciente
        self.descricao = descr
        self.resultado = result

    def imprimir_exame(self):
        print("DADOS / PACIENTE")
        print("Nome: ", self.paciente.nome)
        print("CPF: ", self.paciente.cpf)
        print("Idade: ", self.paciente.idade)
        print("=================================")
        print("DADOS / MÉDICO(a)")
        print("Nome: ", self.medico.nome)
        print("CRM: ", self.medico.crm)
        print("Especialização: ", self.medico.especializacao)
        print("========================================")
        print("Resultado do Exame: ")
        print(self.descricao + ": " + self.resultado)


class Medico:

    def __init__(self, nome, crm, espec):
        self.nome = nome
        self.crm = crm
        self.especializacao = espec


class Paciente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


paciente = Paciente('Marcelo Silva', '587.555.487-55', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')
exame01.imprimir_exame()

paciente2 = Paciente('Jonas Silva', '958.588.888-77', 37)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente2, 'COVID-19', 'Negativo')
exame01.imprimir_exame()

# Deve exibir relatório com todos os dados do exame (inclusive os dados do
# médico e paciente)
