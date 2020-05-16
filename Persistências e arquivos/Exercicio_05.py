import pickle

'''
...continuação do Exercício 04

4 - b) Crie um novo programa. Neste programa, leia o conteúdo do arquivo criado
anteriormente e exiba os dados das contas armazenadas
'''

f = open('C:\\Users\\USUARIO\\Desktop\\JuNiNhOoOo\\Exercícios Python\\Python IMPACTA\\Atividades-Linguagem_II\\Persistências e arquivos\\arquivo_ex_05.py', 'rb')

conta = pickle.load(f)

for i in conta:
    print(conta.nome)