# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface


class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho="pequeno", interface="lcd"):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)

    def print_mp3player(self):
        print("Caracteristicas são " + self.tamanho + " , " + self.interface + " , " + self.capacidade)


deviceSony = MP3Player("128GB")

deviceSony.print_mp3player()
