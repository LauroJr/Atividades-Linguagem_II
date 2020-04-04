''' Exercício 03

Classe Carro:

    Atributos:
        ligado: valor booleano que indica se o carro está ligado ou desligado
        (deve iniciar com o valor False)
        pneu1, pneu2, pneu3, pneu4: objetos do tipo Pneu que representa cada
        um dos pneus do carro (devem receber os valores no construtor).
    Métodos:
        ligar: altera o valor do atributo ligado para True
        desligar: altera o valor do atributo ligado para False
        verificar_pneu: se o carro estiver ligado, esse método deve exibir a
        pressão de cada um dos pneus. Se o carro       estiver desligado, o
        método deve exibir a mensagem ‘Carro Desligado'

Classe Pneu:
    Atributos:
        pressao: valor inteiro que indica a pressão de ar do pneu
        (inicializado no construtor)
    Métodos:
        furar(): simula um pneu furado, alterando o valor do atributo pressao
        para zero.
'''


class Carro:

    def __init__(self, p1, p2, p3, p4):
        self.ligado = False
        self.pneu1 = p1
        self.pneu2 = p2
        self.pneu3 = p3
        self.pneu4 = p4

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def verificar_pneu(self):
        print("Pneu1: ", self.pneu1.pressao)
        print("Pneu2: ", self.pneu2.pressao)
        print("Pneu3: ", self.pneu3.pressao)
        print("Pneu4: ", self.pneu4.pressao)
        if self.ligado is True:
            print("Carro Ligado. Desligue-o")
        elif self.ligado is False and p3.pressao == 0:
            print("O carro está desligado, Agora posso concertá-lo")
        elif p1.pressao > 31:
            print("Carro concertado")


class Pneu:

    def __init__(self, libra):
        self.pressao = libra

    def furar(self):
        self.pressao = 0

    def concertar(self):
        self.pressao = 36


p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro(p1, p2, p3, p4)
meucarro.ligar()
meucarro.verificar_pneu()
meucarro.pneu3.furar()
meucarro.verificar_pneu()  # exibir a pressão de cada pneu.
meucarro.desligar()
meucarro.verificar_pneu()  # exibir mensagem que o carro está desligado
meucarro.pneu3.concertar()
meucarro.verificar_pneu()
