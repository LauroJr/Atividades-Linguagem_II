'''
Exercício 02
Crie uma classe Produto que possua os atributos nome, preco e descricao.
Crie um método exibir_descricao que exibe a descrição do produto.
Crie duas classes filhas de Produto, a classe Mouse com o atributo tipo e a
classe Livro com o atributo autor.
Crie o método exibir_descricao nas classes filhas, que deve exibir a descrição
do produto e o atributo adicional que a classe tiver (“autor” no caso de livro
e “tipo” no caso de mouse)
No programa principal você deve simular a compra de vários mouses e livros, e
inserir todos eles em uma lista chamada carrinho.
Chame o método exibir_descricao para cada objeto do carrinho.
'''


class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def exibir_descricao(self):
        print()
        print(f'Produto: {self.nome}\nPreço: R$ {self.preco}\nDescrição:\
 {self.descricao}')


class Mouse(Produto):
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco, descricao)
        self.tipo = tipo

    def exibir_descricao(self):
        super().exibir_descricao()
        print(f'Tipo: {self.tipo}')


class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor

    def exibir_descricao(self):
        print()
        print(f'Nome do Livro: {self.nome}\nPreço: R$ {self.preco}\nDescrição:\
 {self.descricao}\nAutor: {self.autor}')


print('Execução teste [CELULAR] / Obejto da classe mãe "Produto"')
produto_teste = Produto('Celular', 1500.00, 'Smart Phone')
produto_teste.exibir_descricao()
print()

mouse1 = Mouse('Mouse 1', 22.50, 'Sem fio', 'Arredondado')
mouse2 = Mouse('Mouse 2', 49.90, 'Sem fio', 'quadrangular/ com teclado')
mouse3 = Mouse('Mouse 3', 15.60, 'Com fio', 'universal')

livro1 = Livro('Bíblia', 0.0, 'Distribuição gratuita pela Torre de Vigia',
               'Jeová')

livro2 = Livro('Scrum e XP direto das trincheiras', 90.00, 'T.I',
               'Donalds')
livro3 = Livro('Livro 3', 57.90, 'Aventura', 'Anônimo')

carrinho = [mouse1, mouse2, mouse3, livro1, livro2, livro3]
print('Inicio do programa: ')

for item in carrinho:
    item.exibir_descricao()
