'''Exercício 02 - Classe Triângulo

Crie uma classe que representa um triângulo.
Atributos:
 - lado_a
 - lado_b
 - lado_c
Métodos:
 - calcular_perimetro: retorna o perímetro do triângulo (soma dos três lados)
 - maior_lado: retorna o maior lado do triângulo
Crie um programa que utilize esta classe. O programa deve pedir ao usuário
que informe as medidas dos três lados de um triângulo. Depois deve criar
um objeto com essas medidas e exibir seu perímetro e seu maior lado.'''


class Triangulo:

    def __init__(self):
        self.lado_a = 0
        self.lado_b = 0
        self.lado_c = 0

    def calcular_perimetro(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a + lado_b + lado_c

    def maior_lado(self, lado_a, lado_b, lado_c):
        if lado_a > lado_b and lado_a > lado_c:
            self.lado_b = lado_a
        elif lado_b > lado_a and lado_b > lado_c:
            self.lado_b = lado_b
        else:
            self.lado_b = lado_c


tri = Triangulo()

lado_a = int(input("Lado a: "))
lado_b = int(input("Lado b: "))
lado_c = int(input("Lado c: "))

tri.calcular_perimetro(lado_a, lado_b, lado_c)

tri.maior_lado(lado_a, lado_b, lado_c)

print("O perímetro do triângulo é: ", tri.lado_a)
print("O maior lado do triângulo é: ", tri.lado_b)
