def somar (*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

def sub (a, b):
    sub = a - b
    return sub

def mult (a, b):
    mult = a * b
    return mult

def divi (a, b):
    divi = a / b
    return divi

'''def piramide(n):
    for x in range(number + 1):
        print(str(x) * x)

def coluna(a):
    for x in range(number + 1):
        for y in range(1, x + 1):
            print(y, end=" ")
        print()

number = int(input("Digite um número: "))

coluna(number)'''

def contarVogais(t):

    count = 0

    for x in "O rato roeu a roupa do rei de roma":
        if x in 'AaEeIiOoUu':
            count += 1
    print(count)

def contarLetras(text):

    count = 0
    reverseText = ""

    for x in range(len(text)-1, -1, -1):
        reverseText += text[x]
        if text[x] != " ":
            count += 1

    return count, reverseText


def estoque(a, b, c):
    total = b * c
    return a, total

def list(l):
    b = []
    for x in range(12):
        b.append(l[x])
        if l[x] == x:
            b.remove(l[x])
    return b

def primo(a):
    if a == 1:
        print("Não é primo!")
    elif a == 2:
        print("É primo")
    elif a % 2 == 0:
        print("Não é primo!")
    else:
        if (a % 3 == 0 and a != 3) or (a % 5 == 0 and a != 5) or (a % 7 == 0 and a != 7):
            print("Não é primo!")
        else:
            print("É primo!")
