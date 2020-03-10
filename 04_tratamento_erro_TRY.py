'''' Crie um dicionário (inicialmente vazio) para armazenar uma listagem de
alunos. Nesse dicionário, a chave é o RA do aluno e o valor é o nome do aluno.
Considere que o RA de cada aluno deve ser composto por um número inteiro de
7 dígitos.
Crie uma função que recebe como parâmetros o dicionário, o RA e o nome de um
aluno e insere esse aluno no dicionário.
Caso o RA não esteja no formato correto, deve ser gerada uma exceção do tipo
ValueError
Caso o RA já exista no dicionário, deve ser gerada uma exceção do tipo
TypeError
Crie uma função que recebe como parâmetro o dicionário e o RA de um aluno e
retorna o nome desse aluno. Caso o RA não exista no dicionário, a função
deve gerar uma exceção do tipo KeyError
'''


def inserir_aluno(a, b, c):
    digitos = len(b)
    try:
        if digitos < 7 or digitos > 7:
            raise ValueError
    except ValueError:
        print("RA do aluno deve conter 7 digitos ")
    try:
        b = int(b)
    except ValueError:
        print("Somente valores inteiros")
    else:
        try:
            if b in a:
                raise TypeError
        except TypeError:
            print("RA já cadastrado")
        a[b] = c
    return a


def consulta_aluno(dic, rah):
    if rah in dic:
        a = dic[rah]  # Se o RA estiver no dicionário, ele...
        return a      # ... pega o [valor] que está naquela chave.
    else:
        try:
            raise KeyError
        except KeyError:
            a = "RA inválido"
            return a


dicionario = {}

for i in range(3):
    ra = input("RA com 7 dígitos: ")
    nome = input("Nome: ")
    dicionario_final = inserir_aluno(dicionario, ra, nome)


ra_aluno = int(input("Digite o RA para consulta: "))
d = consulta_aluno(dicionario_final, ra_aluno)
print(d)
