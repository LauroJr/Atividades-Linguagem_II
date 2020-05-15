'''
Exercício 02

- Abra o arquivo criado no exercício anterior. Leia o conteúdo do arquivo e
mostre o somatório de todos os números contidos no arquivo.
'''

ler_arquivo = open('C:\\Users\\USUARIO\\Desktop\\JuNiNhOoOo\\Exercícios Python\\Python IMPACTA\\Atividades-Linguagem_II\\Persistências e arquivos\\arquivo_ex_01.txt', 'r')

conteudo = ler_arquivo.read()

print(f'Leitura do Arquivo .txt: \n{conteudo}')
print(40*'-')
print('Somatória dos números acima: \n')

soma = 0
ler_arquivo_somar = open('C:\\Users\\USUARIO\\Desktop\\JuNiNhOoOo\\Exercícios Python\\Python IMPACTA\\Atividades-Linguagem_II\\Persistências e arquivos\\arquivo_ex_01.txt', 'r')

for num in ler_arquivo_somar:
    soma += int(num)

print(soma)
print()
