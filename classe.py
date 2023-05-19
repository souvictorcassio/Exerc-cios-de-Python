class Pessoa:

    def __init__(self, nome, peso, idade, comendo=False, falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, comida):
        if self.falando == True:
            self.comida = comida
            if not self.comendo == True:
                print(f'{self.nome} foi comer {self.comida}')
                self.comendo = True
            else:
                print(f'{self.nome} já está comendo')
        else:
            print(f'{self.nome} não pode comer porque está falando!')

    def paredecomer(self):
        if self.comendo == True:
            self.comendo = False
            print(f'{self.nome} parou de comer')
        else:
            print(f'{self.nome} não está comendo')

    def falar(self):
        if not self.comendo == True:
            if not self.falando == True:
                self.falando = True
                print(f'{self.nome} começou a falar')
        else:
            print(f'{self.nome} não pode falar porque está comendo')

    def paredefalar(self):
        if self.falando == True:
            self.falando = False
            print(f'{self.nome} parou de falar')
        else:
            print(f'{self.nome} não está falando')

p1 = Pessoa("Victor", 60, 27,)
p2 = Pessoa("Matheus", 65, 27, True)

p1.comer("banana")
p2.comer("maçã")
p2.paredecomer()
p1.falar()
p2.falar()
p2.paredefalar()
p1.paredecomer()
p1.falar()
p1.comer("banana")