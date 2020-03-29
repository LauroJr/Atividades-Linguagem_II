'''Exercício 04 - Classe Aluno

Implemente uma classe Aluno.
Atributos:
 - nome
 - tempo_sem_dormir (em horas. O valor inicial deve ser zero).
Métodos:
 - estudar: recebe como parâmetro de entrada a quantidade de horas
de estudo e acrescenta ao atributo tempo_sem_dormir
 - dormir: recebe como parâmetro de entrada a quantidade de horas de
sono e reduz do atributo tempo_sem_dormir

Faça um programa para criar objeto da classe Aluno e utilize os
métodos estudar e dormir. Ao final exiba quanto tempo o aluno está sem dormir.
'''


class Aluno():
    def __init__(self):
        self.nome = None
        self.tempo_sem_dormir = 0

    def estudar(self, a):
        self.tempo_sem_dormir = a + self.tempo_sem_dormir

    def dormir(self, b):
        self.tempo_sem_dormir = self.tempo_sem_dormir - b


aluno1 = Aluno()
aluno1.nome = "Luizinho"

aluno1.estudar(3)

aluno1.dormir(2)

aluno1.estudar(4)

aluno1.dormir(2)
print('O aluno', aluno1.nome, 'está a', aluno1.tempo_sem_dormir,
      'horas sem dormir')
