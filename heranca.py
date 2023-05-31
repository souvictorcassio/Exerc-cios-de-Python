'''class Animal():
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
vac1.comer()'''

'''class Ingresso():
    def __init__(self, ingresso):
        self.ingresso = ingresso

    def imprimeValor(self):
        print(self.ingresso)

class Vip(Ingresso):
    def __init__(self, ingresso):
        super().__init__(ingresso)

    def imprimeValor(self, percent):
        valorVip = self.ingresso+((self.ingresso*percent)/100)
        print(valorVip)

ig = Vip(20)
ig.imprimeValor(50)'''

'''class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self, altura, base):
        self.area = (altura*base)/2
        print(self.area)

    def calcularPerimetro(self, lado1, lado2, lado3):
        self.perimetro = lado1 + lado2 + lado3
        print(self.perimetro)

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self, altura, base):
        self.area = altura*base
        print(self.area)

    def calcularPerimetro(self, lado1, lado2):
        self.perimetro = (lado1*2) + (lado2*2)
        print(self.perimetro)

tri = Triangulo()

tri.calcularArea(3, 7)
tri.calcularPerimetro(4, 6, 7)

ret = Retangulo()

ret.calcularArea(4, 9)
ret.calcularPerimetro(4, 9)'''

class Atleta():
    def __init__(self, peso, aposentado=False):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        if self.aposentado == True:
            print("Já é aposentado!")
        else:
            self.aposentado == True

    def aquecer(self):
        ...

class Corredor(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def correr(self):
        ...

class Nadador(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def nadar(self):
        ...

class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def pedalar(self):
        ...

class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)