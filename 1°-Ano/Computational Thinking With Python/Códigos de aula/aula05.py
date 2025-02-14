'''
def podeVotar(nome, idade):
    if idade >= 16:
        print(f'Sim, a pessoa {nome} pode votar')
        return True
    else:
        print(f'Não, a pessoa {nome} não pode votar')
        return False
a = podeVotar('Roger', 19)
print(f'A primeira resposta foi: {a}')
b = podeVotar('Heitor', 12)
print(f'A segunda resposta foi: {b}')
---------------------------------------------
def soma(num1, num2):
    return num1 + num2
num1 = input('Diga o 1° número: ')
while not num1.isnumeric():
    num1 = input('Diga o 1° número: ')
num2 = input('Diga o 2° número: ')
while not num2.isnumeric():
    num2 = input('Diga o 2° número: ')
num1 = int(num1)
num2 = int(num2)
print()
print(f'{num1} + {num2} = {soma(num1, num2)}')
---------------------------------------------
def idade(nome, anoNascimento):
    idade = 2024 - anoNascimento
    print(f'{nome}, têm {idade} anos')
    return idade
nome = input('Diga seu nome: ')
anoNascimento = input('Diga o ano de seu nacimento: ')
while not anoNascimento.isnumeric():
    anoNascimento = input('Diga o ano de seu nacimento: ')
anoNascimento = int(anoNascimento)
resposta = idade(nome, anoNascimento)
print(resposta)
---------------------------------------------
def idade(nome, anoNascimento):
    print(f'{nome}, têm {2024 - anoNascimento} anos.')
    return 2024 - anoNascimento
a = idade('Roger', 2004)
print(a)
---------------------------------------------
lista_apresentacao = []
def apresentacao(nome, idade, sexo, estado_civil):
    resposta = print(f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}\nEstado Civíl: {estado_civil}')
    return resposta
nome = input('Diga o seu nome: ')
lista_apresentacao.append(nome)
idade = int(input('Diga a sua idade: '))
lista_apresentacao.append(idade)
sexo = input('Diga seu sexo biológico: ')
lista_apresentacao.append(sexo)
est_civil = input('Diga o seu estado civíl: ')
lista_apresentacao.append(est_civil)
print(lista_apresentacao)
def maior_numero(numeros):
    maior = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
    return print(f'Lista: {numeros}\nO maior número da lista é {maior}')
maior_numero([1000, 20, 230, 26, 470, 11])
---------------------------------------------
def maior_numero(numeros):
    maior = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
    return print(f'Lista: {numeros}\nO maior número da lista é {maior}')
maior_numero([1000, 20, 230, 26, 470, 11])
maior_numero([-1, -3, -4, -2])
---------------------------------------------
def momento_adiante(hora, minuto):
    minuto += 1
    if hora == 23 and minuto == 60:
        return print(f'Próximo horário: 00:00')
    if minuto == 60:
        minuto = 0
        hora += 1
        return print(f'Próximo horário: {hora} horas e 0{minuto} minutos.')
    if minuto < 10:
        return print(f'Próximo horário: {hora} horas e 0{minuto} minutos.')
    return print(f'Próximo horário: {hora} horas e {minuto} minutos.')
hora = int(input('Digite as horas: '))
minuto = int(input('Agora digite os minutos: '))
momento_adiante(hora, minuto)
---------------------------------------------
def pega_numero():
    while True:
        a = input('Diga um número positivo: ')
        if a.isnumeric():
            a = int(a)
            return print(f'Número positivo digitado foi {a}.')
pega_numero()
---------------------------------------------
def tel_valido(telefone):
    if len(telefone) >= 8 and len(telefone) <= 11 and telefone.isnumeric():
        return print(f'Seu telefone {telefone} é válido.')
    else:
        return print(f'Este telefone é inválido!')
tel_valido('11998451244')
tel_valido('998451244')
tel_valido('12345678')
tel_valido('1234567899')
tel_valido('1234')
tel_valido('aaa')
---------------------------------------------
def tel_valido(telefone):
    if len(telefone) >= 8 and len(telefone) <= 11 and telefone.isnumeric():
        return True
telefone = input('Digite seu telefone: ')
while not tel_valido(telefone):
    print(f'Este telefone {telefone} é inválido! Digite novamente.')
    telefone = input('Digite seu telefone: ')
print(f'Legal telefone {telefone} é válido.')
---------------------------------------------
lista_carros = ['HB20', 'Sandero', 'Uno', 'Celta', 'Fusca']
def verifica_carro(carro):
    for i in range(len(lista_carros)):
        if carro == lista_carros[i]:
            return True
carro_digitado = input('Qual o seu carro? ')
while not verifica_carro(carro_digitado):
    print(f'{carro_digitado} não está na lista!')
    carro_digitado = input('Qual o seu carro? ')
print(f'{carro_digitado} está na lista.')
---------------------------------------------
lista_carros = ['HB20', 'Sandero', 'Uno', 'Celta', 'Fusca']
def verifica_carro(carro):
    if carro in lista_carros:
        return True
carro_digitado = input('Qual o seu carro? ')
while not verifica_carro(carro_digitado):
    print(f'{carro_digitado} não está na lista!')
    carro_digitado = input('Qual o seu carro? ')
print(f'{carro_digitado} está na lista.')
---------------------------------------------
import random
num_secreto = random.randint(1, 100)
def verifica_num(numero):
    if numero == num_secreto:
        return True
num = int(input('Digite um número de 1 a 100: '))
while not verifica_num(num):
    if num < num_secreto:
        print(f'{num} não é o número secreto, ele é menor!')
    else:
        print(f'{num} não é o número secreto, ele é maior!')
    num = int(input('Digite um número de 1 a 100: '))
print('Você acertou o número secreto!')
---------------------------------------------
def tem_numero_impar(lista):
    for num in lista:
        if num % 2 == 1:
            return True
    return False
a = tem_numero_impar([12, 3, 4, 7, 11])
print(a)
'''
