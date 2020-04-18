''' Atributos ou métodos com nomes iniciados por dois sublinhados são privados
e todas as outras formas são públicas.
Os atributos ou métodos PRIVADOS mão poderm ser acessados fora da classe.'
'''


class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__rg = rg

    def exibir_dados(self):
        print(f'CPF: {self.__cpf}\nRG: {self.__rg}')


objeto_pessoa1 = Pessoa('Lauro Jr', '27', '408.850.168/31', '48.187.272-3')
objeto_pessoa1.nome = 'Lauro Mendes do Amaral Junior'
objeto_pessoa1.idade = '28'
print(f'{objeto_pessoa1.nome} tem a seguinte idade: {objeto_pessoa1.idade}\
 anos')

#objeto_pessoa1.__cpf = 'teste teste'
#print(objeto_pessoa1.__cpf)  # Erro (este atributo é privado)

objeto_pessoa1.exibir_dados()
