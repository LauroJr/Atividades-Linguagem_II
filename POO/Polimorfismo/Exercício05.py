'''
Exercício 05

Um banco trabalha com três tipos de contas:
- conta corrente comum
- conta corrente com limite
- conta poupança
Em todos os casos é necessário guardar o número da conta, o nome do
correntista e o saldo.
Para a conta poupança é necessário guardar o dia do aniversário da conta
(quando são creditados os juros).
Já para a conta com limite é necessário guardar o valor do limite.
As operações possíveis são: depósito, saque e impressão de saldo.
Essas operações devem ser definidas numa classe abstrata denominada Conta.
A operação de depósito e saldo são iguais para os três tipos de conta.
A operação de saque só é diferente na conta com limite, pois esta admite que o
saldo fique negativo até o limite estabelecido.
Nas demais contas o saque não pode ser realizado se não houver saldo
suficiente.
Implemente a hierarquia de classes definida acima.
'''

from abc import ABC, abstractmethod
import time
import os


def carregando():
    for i in range(101):
        print("Contagem das cédulas...")
        print(f"{i}%")
        print(i*'◼')
        time.sleep(0.02)
        os.system("cls")
    print('Saque o dinheiro no caixa')


class Conta(ABC):
    num_conta = None
    nome_correntista = None
    saldo_conta = 0.00

    @abstractmethod
    def deposito(self, valor):
        pass

    @abstractmethod
    def saque(self, valor):
        pass

    @abstractmethod
    def impressao_saldo(self):
        pass


class Poupanca(Conta):
    def __init__(self, num_conta, nome_correntista, aniv_conta_juros):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.aniv_conta_juros = aniv_conta_juros

    def deposito(self, valor):
        self.saldo_conta += valor

    def saque(self, valor):
        self.saldo_conta -= valor
        if self.saldo_conta < 0:
            self.saldo_conta += valor
            print('Conta sem saldo. Impossível realizar saque :( ')
        else:
            print('TRANSAÇÃO ACEITA')
            carregando()

    def impressao_saldo(self):
        print('Conta Poupança')
        print(f'EXTRATO\nNome: {self.nome_correntista}\nConta: {self.num_conta}\n\
Saldo: {self.saldo_conta}\nData p/ crédito de juros: {self.aniv_conta_juros}')


class Ccc(Conta):
    def __init__(self, num_conta, nome_correntista):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista

    def deposito(self, valor):
        self.saldo_conta += valor

    def saque(self, valor):
        self.saldo_conta -= valor
        if self.saldo_conta < 0:
            self.saldo_conta += valor
            print('Conta sem saldo. Impossível realizar saque :( ')
        else:
            print('TRANSAÇÃO ACEITA')
            carregando()

    def impressao_saldo(self):
        print('Conta correte com Comun')
        print(f'EXTRATO\nNome: {self.nome_correntista}\nConta: {self.num_conta}\n\
Saldo: {self.saldo_conta}')


class Ccl(Conta):
    def __init__(self, num_conta, nome_correntista, limite):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.limite = limite

    def deposito(self, valor):
        self.saldo_conta += valor

    def saque(self, valor):
        limite = self.limite
        self.limite = self.limite - self.limite - self.limite
        self.saldo_conta -= valor
        if self.saldo_conta < self.limite:
            self.limite = limite
            self.saldo_conta += valor
            print('Conta sem saldo. Limite ultrapassado. Impossível realizar\
 saque :( ')
        else:
            print('TRANSAÇÃO ACEITA')
            carregando()

    def impressao_saldo(self):
        print('Conta correte com Limite')
        print(f'EXTRATO\nNome: {self.nome_correntista}\nConta: {self.num_conta}\n\
Saldo: {self.saldo_conta}\nLimite: {self.limite}')


#poup = Poupanca('0003598-3', 'Lauro Mendes do Amaral Junior', '12/05/2020')
#poup.deposito(150)
#poup.saque(151)
#poup.impressao_saldo()
# print('----------------------------------------------------------------------')
#ccl = Ccl('0003267-8', 'João Gonçalves da Silva', 500)
#ccl.deposito(350)
#ccl.saque(855)
#ccl.impressao_saldo()
# print('----------------------------------------------------------------------')
ccc = Ccc('0003256-5', 'Stev Jobs')
ccc.deposito(240)
ccc.saque(245)
ccc.impressao_saldo()
