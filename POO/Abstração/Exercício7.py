'''Exercício 07

Implemente as classes Produto e Pedido.

Classe Pedido:
    Atributos:
        produtos: Lista de objetos do classe Produto
    Métodos:
        adicionar_produto: recebe um objeto Produto e o adiciona na lista de
        produtos.
        calcular_valor: deve retornar o valor total do pedido (soma dos
        valores de todos os produtos do pedido)

Classe Produto:
    Atributos:
        nome: nome do produto
        preco: preço do produto
        quantidade: quantidade de itens do produto
    Métodos:
        Não possui
'''


class Pedido:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, prod):
        self.produtos.append(prod)

    def calcular_valor(self):
        soma = 0
        for itens in self.produtos:
            soma += (itens.preco * itens.quantidade)
        return soma


class Produto:

    def __init__(self, nome_prod, preco_prod, qnt_prod):
        self.nome = nome_prod
        self.preco = preco_prod
        self.quantidade = qnt_prod


cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())	     # imprime 20.90
# print("Lista completa: ",meu_pedido.produtos.nome.preco.quantidade)
