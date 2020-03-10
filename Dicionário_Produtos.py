produtos = {}
lista = []
c = 0

while c < 5:
    nome_produto = input("Nome do produto: ")
    preço_produto = float(input("Valor do produto: "))
    c = c + 1
    produtos[nome_produto] = preço_produto
    

for Item in produtos:
    if produtos[Item] > 50:
        print(Item, produtos[Item])
