"""soma = 0
cont = 0

while cont < 10:
    num = float(input("Digite algum número"))
    soma = soma + num
    cont = cont + 1
print(soma/cont)"""

"""numbStudent = int(input("Digite a quantidade de alunos"))
cont = 1
soma = 0

while cont <= numbStudent:
    nota = float(input("Digite a nota do aluno"))
    soma+=nota
    cont+=1

print(soma/numbStudent)"""

"""inc = int(input("Digite um 1 para iniciar: "))

while inc == 1:
    numb1 = float(input("Digite o  primeiro numero: "))
    numb2 = float(input("Digite o  segundo numero: "))

    if numb2 <= 0:
        print("Número menor ou igual a zero")
    else:
        print("O valor da divisão é ", numb1 / numb2)
    inc = int(input("Digite um 1 para iniciar: "))"""

'''pin = "123"
senha = input("Digite sua senha: ")
cont = 1
tent = 2

while senha != pin:

    print("Acesso negado!")
    print("Você tem mais ", tent, " tentativa(s)")
    senha=input()
    cont += 1
    tent -= 1
    if cont >= 3:
        print("Senha bloqueada!")
        break
else:
     print("Acesso permitido!")'''

'''menu = 1

while menu == 1:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    if nota1 > 10 or nota2 > 10:
        print("A nota deve possuir valor entre 0 a 10")
    elif nota1 < 0 or nota2 < 0:
        print("A nota deve possuir valor entre 0 a 10")
    else:
        media = (nota1 + nota2) / 2
        print("A média calculada é ", media)
    menu = int(input("Digite 1 para continuar: "))'''

'''number = int(input("Digite um número: "))
for x in range(number+1):
    for y in range(x):
        print(x, end="")
    print()'''

'''for x in range(5):
    for y in range(x):
        print(y, end="")
    print()'''

'''quantidade=int(input("Digite a quantidade de alunos: "))
nomeAlunos=[]

for x in range(quantidade):
    nomeAlunos.append(input("Digite o nome do aluno: "))

pesquisa=input("Digite o nome para pesquisa: ")
cont=0
for y in range(quantidade):
    if pesquisa == nomeAlunos[y]:
        print(y, nomeAlunos[y])
    else:
        cont+=1
if cont == quantidade:
    print("Não encontrado!")'''

'''notaTurma=[]
cont = 0
soma = 0

for x in range(5):
    notaTurma.append(float(input("Digite as notas da Turma 5: ")))

for y in range(5):
    soma = soma + notaTurma[y]

media = soma/5

for z in range(5):
    if notaTurma[z] >= media:
        cont+=1

print("A media da turma é ", media, "e", cont, "nota(s) acima da média!")'''

'''numbers = []
result = []

for x in range(10):
    numbers.append(float(input("Digite um número: ")))

mult = int(input("Digite um número para multiplicar: "))

for y in range(10):
    result.append(numbers[y]*mult)

print("Primeira lista ->", numbers)
print("Multiplicador -> ", mult)
print("Segunda lista -> ", result)'''

'''a = []

for x in range(5):
    a.append(int(input("Digite um número: ")))

print(a)

for y in range(4, -1, -1):
    print(a[y])'''

'''users = []
pin = []

for x in range(5):
    users.append(input("Digite o seu usuario: "))
    pin.append(input("Digite a sua senha: "))

for y in range(5):
    print("Usuário", users[y], "na posição", y)
    print("Possui a senha:", pin[y])

for z in range(3):
    userLogin = input("Digite a seu usuário: ")
    pinLogin = input("Digite a sua senha: ")

    if userLogin == users[x] and pinLogin == pin[x]:
        print("Bem vindo!", users[x])
        print("Login efetuado com sucesso!")
        break
    else:
        print("Usuário inválido!")'''

'''number = int(input("Digite um número: "))

a = []
b = []
soma = []

for x in range(number):
    a.append(float(input("Digite um número de novo: ")))
    b.append(float(input("Digite mais um número: ")))

for y in range(number):
    soma.append(a[y]+b[y])

print(soma)'''

'''lista = []
cont = 0

for x in range(10):
    lista.append(int(input("Digite um número: ")))

number = int(input("Digite outro número: "))

for y in range(10):
    if number == lista[y]:
        cont = cont + 1

print("O número", number, "apareceu", cont, "vez(es)")'''

'''nomes = []

for x in range(5):
    nomes.append(input("Informe o seu nome: "))

print(nomes)

for y in range(4, -1, -1):
    print(nomes[y])'''

'''numbers = []
cont = 0
soma = 0

for x in range(10):
    numbers.append(int(input("Digite um número: ")))

for y in range(10):
    if numbers[y] % 2 == 0:
        print("Número par:", numbers[y])
    else:
        print("Número impar:", numbers[y])

maior = numbers[0]

for z in range(10):
    if numbers[z] > maior:
        maior = numbers[z]

menor = numbers[0]

for xx in range(10):
    if numbers[xx] < menor:
        menor = numbers[xx]

print("O maior número é", maior, "e o menor número é", menor)

for yy in range(10):
    soma = soma + numbers[yy]

media = soma / 10

for zz in range(10):
    if numbers[zz] > media:
        cont += 1

print("A média é ", media, "e", cont, "número(s) maior(es) que a média")'''

'''x = 0
med = []

while x == 0:

    nota1 = float(input("Digite a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    med.append(media)

    if media >= 7:
        print("Aluno aprovado!")
    elif media >= 4:
        print("Aluno em recuperação!")
    else:
        print("Aluno reprovado!")

    x = int(input("Deseja continuar? Digite 0. Informe qualquer outro número para encerrar "))

print("Conjunto de média da turma: ", med)'''

'''resp = "sim"

while resp == "sim":

    number = int(input("Digite um número: "))

    if number != 0:
        if number > 0:
            print("O número é positivo")
        else:
            print("O numero é negativo")
    else:
        print("O número é igual a ZERO!")

    resp = input("Deseja continuar? Digite 'sim'. Informe qualquer outro número para encerrar ")'''

'''age = int(input("Digite a sua idade: "))

print("O ano em que nasceu é", 2023-age)'''

'''number = int(input("Digite um número: "))

if number >= 0:
    if number % 2 == 0:
        print("O número é par e positivo!")
    else:
        print("O número é impar e positivo!")
else:
    if number % 2 == 0:
        print("O número é par e negativo!")
    else:
        print("O número é impar e negativo!")'''

'''number1 = float(input("Digite um número: "))

number2 = float(input("Digite outro número: "))

number3 = float(input("Digite mais um número: "))

if number1 > number2 and number1 > number3:
    print("O maior número é", number1)
elif number2 > number3:
    print("O maior número é", number2)
else:
    print("O maior número é", number3)'''

'''number = int(input("Digite um número: "))

if number > 0:
    print("O antecessor é", number - 1)
else:
    print("O antecessor é", number + 1)'''

'''dia = int(input("Digite o dia em que nasceu"))

mes = int(input("Digite o mês em que nasceu"))

ano = int(input("Digite o ano em que nasceu"))

dias = ((2023-ano)*365) + mes * 30 + dia

print(dias)'''

'''quantEleitores = int(input("Digite a quantidade de eleitores: "))

validos = int(input("Número de votos válidos: "))

brancos = int(input("Número de votos em branco: "))

nulos = int(input("Número de votos nulos: "))

print("A votação foi encerrado e o resultado foi: ")
print("Votos válidos", validos, "porcentagem de", (validos*quantEleitores)/100)
print("Votos em branco", brancos, "porcentagem de", (brancos*quantEleitores)/100)
print("Votos nulos", nulos, "porcentagem de", (nulos*quantEleitores)/100)'''