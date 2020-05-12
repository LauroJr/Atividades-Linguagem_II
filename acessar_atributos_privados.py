class Pessoa:
    def __init__(self, nome, documentos, idade, fone):
        self.__nome = nome
        self.__documentos = documentos
        self.__idade = idade
        self.__fone = fone

    def get_documento(self):
        return self.__documentos


class Documentos:
    def __init__(self, cpf, rg, reservista):
        self.__cpf = cpf
        self.__rg = rg
        self.__reservista = reservista

    def get_cpf(self):
        return self.__cpf


doc1 = Documentos('123.456.789-10', '85.895.867-7', '1245 6587')
pessoa1 = Pessoa('João', doc1, '18', '(11)2020-3030')

print(pessoa1.get_documento().get_cpf())
