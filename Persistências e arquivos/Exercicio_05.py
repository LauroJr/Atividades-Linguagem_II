import pickle

'''
...continuação do Exercício 04

4 - b) Crie um novo programa. Neste programa, leia o conteúdo do arquivo criado
anteriormente e exiba os dados das contas armazenadas
'''


class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo


f = open('C:\\Users\\USUARIO\\Desktop\\JuNiNhOoOo\\Exercícios Python\\Python IMPACTA\\Atividades-Linguagem_II\\Persistências e arquivos\\contas.txt', 'rb')

conta = pickle.load(f)

for i in conta:
    print("Numero:", i.numero)
    print("Titular:", i.titular)
    print("Saldo:", i.saldo)
    print("-" * 10)
    print()

f.close()
