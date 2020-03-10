''' Nesta questão você deve identificar as partes problemáticas do código e
reescrevê-lo utilizando tratamento de exceções. Ou seja, devem ser
identificadas todas as exceções que podem ser geradas e, para cada uma,
deve ser dado o tratamento adequado que, nesse exercício, significa alertar
o usuário quanto ao problema. Entretanto, nesse programa a leitura dos valores
deve ser feita, mesmo que para isso o usuário tenha que tentar informar várias
vezes os valores na mesma execução do programa.
'''

continuar = True

while continuar:
    try:
        x = int(input('Primeiro valor: '))
        y = int(input('Segundo valor: '))
        z = x / y
    except ZeroDivisionError:
        print("ERRO. Impossível divisão por zero")
    except ValueError:
        print("Entre com um valor válido")
    except Exception:
        print("Algo deu errado. Entre com dados válidos")
    else:
        continuar = False
        print('O resultado da divisão é:', z)
