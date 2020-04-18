''' Atributos ou métodos com nomes iniciados por dois sublinhados são privados
e todas as outras formas são públicas.
Os atributos ou métodos PRIVADOS mão poderm ser acessados fora da classe.'

Métodos get: Retorna valor do atributo
Métodos set: Altera o valor do atributo
Ambos podem ser utilizados para realizar validação de acesso
'''


class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__rg = rg

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_rg(self, rg):
        self.__rg = rg


objeto_pessoa1 = Pessoa('Lauro Jr', '27', '408.850.168/31', '48.187.272-3')
objeto_pessoa1.nome = 'Lauro Mendes do Amaral Junior'
objeto_pessoa1.idade = '28'
objeto_pessoa1.set_cpf('111.222.333/44')
print("CPF: ", objeto_pessoa1.get_cpf())
