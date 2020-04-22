'''Exercício 01 - Classe Televisão
Implemente uma classe Televisao.
Atributos:
canal (o canal inicial da tv deve ser None)
volume (o volume inicial da tv deve ser zero)
Métodos:
aumentar_volume: aumenta o nível de volume em uma unidade
diminuir_volume: diminui o nível de volume em uma unidade
alterar_canal: recebe o número do canal que será sintonizado e altera o canal
da tv.
Faça um programa para criar um objeto Televisao e testar a sua classe.
'''


class Televisao:

    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self, vol):
        '''Esta função recebe o parâmetro VOL, que é o volume atual da tv
        e tem por objetivo aumentar o volume.
        '''
        aumentar = int(input("Aumente o volume: "))
        self.volume = aumentar + vol

    def diminuir_volume(self, vol):
        '''Esta função recebe o parâmetro VOL, que é o volume atual da tv
        e tem por objetivo diminuir o volume.
        '''
        diminuir = int(input("Diminua o volume: "))
        self.volume = vol - diminuir

    def alterar_canal(self, n_canal):
        '''Esta função recebe o parâmetro n_canal, que contém o valor do canal já
        pré-definido (poderia ser digitado pelo usuário também), e tem por
        objetivo alterar o canal de acordo com o parâmetro passado.
        '''
        self.canal = n_canal


# Todo comando que tiver "tv.alguma_coisa", está chamando um método
tv = Televisao()  # A variável tv está recebendo td minha classe definida acima
tv.alterar_canal(5)  # chamei o método alterar_canal(função dentro da classe)

vol = 0  # preciso desse parâmetro dentro dos meus métodos de aum(+) e dim(-)
tv.aumentar_volume(vol)
vol = vol + tv.volume

tv.aumentar_volume(vol)
vol = 0
vol = vol + tv.volume

tv.aumentar_volume(vol)
vol = 0
vol = vol + tv.volume

tv.diminuir_volume(vol)

print('A tv está no canal:', tv.canal)
print('A tv está no volume:', tv.volume)
