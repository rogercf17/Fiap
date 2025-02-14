'''
string = 'Hello World!'
inteiro = 10
flutuante = 4.5
booleano = True
print(type(string))
print(type(inteiro))
print(type(flutuante))
print(type(booleano))
'''
'''
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
print(f'{a} mais {b} = {soma}') f antes das aspas simples é para colocar a váriavel, como se fosse um format
print(f'{a} menos {b} = {subtracao}')
print(f'{a} vezes {b} = {multiplicacao}')
print(f'{a} dividido por {b} = {divisao}')
'''
'''
a = 1
b = 2
aux = a
print(a, b)
a = b
b = aux
print(a, b)
'''
'''
nome = input("Digite seu nome: ")
frase = "Eu"
print(frase)
frase = frase + " sou"
print(frase)
frase = frase + " o"
print(frase)
frase = frase + " " + nome
print(frase)
'''
'''
resultado1 = 2 < 3
print(resultado1)
resultado2 = 2 > 3
print(resultado2)
resultado3 = 2 <= 3
print(resultado3)
resultado4 = 2 >= 3
print(resultado4)
resultado5 = 2 == 3
print(resultado5)
resultado6 = 2 != 3
print(resultado6)
resultado7 = not 2 == 3
print(resultado7)
print(type(2) is int)
'''
print(2<3 and 3>4)
print(2<3 or 3>4)