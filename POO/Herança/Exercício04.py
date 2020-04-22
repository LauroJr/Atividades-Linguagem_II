'''Exercício 04
Implemente o diagrama de classes apresentado abaixo.
Em seguida:
- Crie um objeto do tipo cachorro e faça-o pedir comida.
- Crie um objeto do tipo gato e faça-o pedir comida.
'''


class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def emitir_som(self):
        print(self.som)


class Cachorro(Animal):
    def __init__(self, nome, som, raca):
        super().__init__(nome, som)
        self.raca = raca

    def pedir_comida(self):
        print('Abana o rabo')


class Gato(Animal):
    def __init__(self, nome, som, cor):
        super().__init__(nome, som)
        self.cor = cor

    def pedir_comida(self):
        print('Gato faz olhar triste')


cachorro = Cachorro('Pitoco', 'au..au..au', 'Pitbull')
print(cachorro.nome)
print(cachorro.raca)
cachorro.emitir_som()
cachorro.pedir_comida()
print()
gato = Gato('Sheik', 'miau...miau', 'Branco')
print(gato.nome)
print(gato.cor)
gato.emitir_som()
gato.pedir_comida()
