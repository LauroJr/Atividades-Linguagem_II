''' O código abaixo lança uma exceção e interrompe a execução do programa.
Utilizando o tratamento de exceções, corrija o programa com o objetivo de
não parar sua execução. Obs: A exceção gerada dever ser do tipo IndexError
'''


def funcao_1():
    print('Início da função 1')
    funcao_2()
    print('Fim da função 1')


def funcao_2():
    print('Início da função 2')
    try:
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i])
    except IndexError:
        print("ERRO. Lista falta números")
        print('Volte e preencha os dados corretamente')
    else:
        print('Fim da função 2')


print('Início do programa')
funcao_1()
print('Fim do programa')
