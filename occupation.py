''' Encontramos neste programa várias funções criadas, para serem importadas para outro programa.
     Dessa forma ganhamos tempo sem precisar ficar codando tudo denovo uma vez que o código já está pronto
     OBS: Para importar, abra um NEW FILE , e use  FROM (occupation) IMPORT (nome da função). Explicação:
     occupation é o nome da pasta de onde será importado a sua função. '''


def calcula_soma(a, b):   # FUNÇÃO P/ CALCULAR DOIS NÚMEROS
    soma = a + b
    return soma    # retorna o valor para o programa ao qual será importado essa função
####################################################################################################################


def intercala():   # FUNÇÃO QUE CONCATENA DUAS TUPLAS
    tupla1 = ()
    tupla2 = ()
    tupla_Concatenada = ()
    print("PRIMEIRA TUPLA: ")
    for I in range(3):
        n = int(input("Digite um número : "))
        tupla1 = tupla1 + (n,)
    print("")
    print("SEGUNDA TUPLA: ")
    for I in range(3):
        n = int(input("Digite um número : "))
        tupla2 = tupla2 + (n,)
    tupla_Concatenada = tupla1 + tupla2
    tupla_real = ()
    cont1 = 0
    cont2 = 3
    c1 = 0
    c2 = 3
    while cont1 <= 2:
        n1 = tupla_Concatenada[c1]
        n2 = tupla_Concatenada[c2]
        tupla_real = tupla_real + (n1,) + (n2,)
        cont1 = cont1 + 1
        cont2 = cont2 + 1
        c1 = c1+1
        c2 = c2+1
    # tupla_Concatenada = tupla_real
    print("")
    return tupla_real


def soma(a):
    s = 0
    for I in a:
        s = s+I
    return s
