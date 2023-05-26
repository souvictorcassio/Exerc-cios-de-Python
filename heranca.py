class Animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def emitir_som(self):
        print(f'{self.nome} {self.cor} está emitindo som')

    def comer(self):
        print(f'{self.nome} vai comer')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f'O gato {self.nome} {self.cor} foi miar')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f'O cachorro {self.nome} {self.cor} foi latir')

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

gt1 = Gato("Bibi", "preto")
cch1 = Cachorro("Pringles", "caramelo")
vac1 = Vaca("Berenilce", "toddy")

gt1.emitir_som()
cch1.emitir_som()
vac1.emitir_som()
vac1.comer()