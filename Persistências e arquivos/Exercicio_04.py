import pickle

'''
Exercício 04

a) Faça uma classe Conta, com os atributos:
- numero
- titular
- saldo

Crie uma lista com 3 objetos da classe Conta.

Armazene a lista de contas em um arquivo utilizando o módulo pickle.
'''


class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo


cliente_01 = Conta('Lauro Mendes do Amaral Junior', 1, 12000.00)
cliente_02 = Conta('Mariana Araújo da Silva', 2, 15000.00)
cliente_03 = Conta('Daniel Mendes do Amaral', 3, 13500.00)

lista_clientes = [cliente_01, cliente_02, cliente_03]

f = open('C:\\Users\\USUARIO\\Desktop\\JuNiNhOoOo\\Exercícios Python\\Python IMPACTA\\Atividades-Linguagem_II\\Persistências e arquivos\\contas.txt', 'wb')

pickle.dump(lista_clientes, f)
f.close()


'''
b) Crie um novo programa. Neste programa, leia o conteúdo do arquivo criado
anteriormente e exiba os dados das contas armazenadas

Continua no Exercício 05...
'''
