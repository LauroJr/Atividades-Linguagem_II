''' Exercício 02
Crie a classe Animal com os atributos nome, cor e numero_patas. Crie também
o método
exibir_dados, que imprime na tela uma espécie de relatório informando os dados
do animal.
Crie uma classe Cachorro que herde da classe Animal e que possui como atributo
adicional a raça
do cachorro. Crie também o método exibir_dados, que imprime na tela os dados
do cachorro
(nome, cor, numero de patas e raça)
'''


class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print(self.nome)
        print(self.cor)
        print(self.numero_patas)


class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca

    def exibir_dados(self):
        super().exibir_dados()
        print(self.raca)


animal = Animal('Pato', 'Branco', 2)
animal.exibir_dados()
print()
cachorro = Cachorro('Bilu', 'Preto', 4, 'Pastor Alemão')
cachorro.exibir_dados()
