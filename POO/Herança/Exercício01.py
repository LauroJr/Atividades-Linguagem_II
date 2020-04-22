'''Exercício 01
Na UML, a herança é representada por uma seta com um triângulo em uma das
extremidades.
Esse triângulo sempre aponta para a superclasse (classe mãe).
O diagrama abaixo fornece uma hierarquia de classes onde a classe Pessoa é a
superclasse
(classe mãe), e as classes PessoaFisica e PessoaJuridica são as subclasses
(classes filhas).
Crie uma classe Pessoa com os atributos id e nome.
Crie uma classe PessoaJuridica que herda da classe Pessoa e acrescenta o
atributo cnpj.
Crie uma classe PessoaFisica que herda da classe Pessoa e acrescenta os
atributos rg e cpf.
'''


class Pessoa:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class PessoaJuridica(Pessoa):
    def __init__(self, id, nome, cnpj):
        super().__init__(id, nome)
        self.cnpj = cnpj


class PessoaFisica(Pessoa):
    def __init__(self, id, nome, rg, cpf):
        super().__init__(id, nome,)
        self.rg = rg
        self.cpf = cpf


pessoa1 = Pessoa(1, "Nome da Pessoa")
p_juridica = PessoaJuridica(2, "Nome da Pessoa Juridica", "1111111111")
p_fisica = PessoaFisica(3, "Nome da Pessoa Fisica", "222222222", "333333333")
print(pessoa1.id)       # 1
print(pessoa1.nome)     # Nome da Pessoa
print(p_juridica.id)    # 2
print(p_juridica.nome)  # Nome da Pessoa Juridica
print(p_juridica.cnpj)  # 1111111111
print(p_fisica.id)      # 3
print(p_fisica.nome)    # Nome da Pessoa Fisica
print(p_fisica.rg)      # 222222222
print(p_fisica.cpf)     # 333333333
