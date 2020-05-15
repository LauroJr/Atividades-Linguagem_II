'''
Exercício 03

- Faça um programa que leia um arquivo texto, lendo linha a linha, e exibindo
cada uma das linhas numeradas na tela.
A ideia é podermos pegar um arquivo de texto qualquer (pode ser inclusive o
arquivo de um programa fonte (arquivo .py) de um dos exercícios anteriores) e
mostrar na tela com as linhas numeradas.
As primeiras linhas do arquivo iriam ser exibidas na tela de forma semelhante
ao exemplo abaixo:
Linha 1 :   class Pessoa:
Linha 2 :       def __init__(self, nome, idade):
Linha 3 :           self.nome = nome
Linha 4 :           self.idade = idade
Linha 5 :
Linha 6 :   p = Pessoa("Maria", 22)
'''

lendo_linhas = open('C:\\Users\\USUARIO\\Desktop\\JuNiNhOoOo\\Exercícios Python\\Python IMPACTA\\Atividades-Linguagem_II\\Persistências e arquivos\\01_Atividade_de_frequencia_arquivo_textos.py', 'r')

c = 1
for linhas in lendo_linhas:
    linhas = linhas.rstrip()
    if c < 10:
        print(f'  {c} : ', linhas)
    else:
        print(f' {c} : ', linhas)
    c += 1
