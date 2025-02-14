'''
for i in range(10):
    print(i)
print(i)
-----------------------------------
for i in range(1, 10, 2):
    print(i)
print()
for i in range(10, 1, -2):
    print(i)
-----------------------------------
for i in range(10):
    print(i, end=' ')
    i = 1
    print(i)
for i in range(10):
    print(i, end='')
    i = 1
    print(i)
-----------------------------------
# TABUADA
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}')
    print()
-----------------------------------
# SOMA
soma = 0
for i in range(1, 101):
    soma += i
print(soma)
-----------------------------------
# SENHA CADASTRADA
senha_cadastrada = '12345'
for i in range(3):
    senha = input('Digite a senha: ')
    if senha == senha_cadastrada:
        print('Acesso liberado!')
        break
    print(f'Você é hacker?? só mais {2-i} tentativas!')
if senha != senha_cadastrada:
    print('Sai hacker!')
-----------------------------------
# TOTAL DE PARES
par = 0
for i in range(10):
    num = input('Diga um número: ')
    while not num.isnumeric():
        print('Deve ser um número!')
        num = input('Diga um número: ')
    num = int(num)
    if num % 2 == 0:
        par += 1
print(f'Total pares = {par}\nTotal ímpares = {(i+1)-par}')
-----------------------------------
lista = [True, 1, 2.5, [], 'kkkk']
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
lista[0] = False
lista[4] = 'kkkk mt bom'
print(lista)
lista.append(5)
print(lista)
-----------------------------------
professores = ['Danilo', 'Lucas Demetrius', 'Lucas Silva', 'Jones', 'Caio', 'Ana', 'Cordeiro']
for i in professores:
    print(i)
print()
for i in range(len(professores)):
    print(professores[i])
print()
for i in professores:
    i = 1
print(professores)
print()
for i in range(len(professores)):
    professores[i] = 1
print(professores)
-----------------------------------
lista = [1, 4, 6, 18, 23]
escolha = input(f'Está é a lista {lista}\nDeseja altera-lá?')
if escolha == 'não':
    print('Ok boa noite!')
else:
    for i in range(len(lista)):
        num = int(input(f'Digite o número para indice {i}: '))
        lista[i] = num
    print(f'Está é a nova lista: {lista}')
-----------------------------------
# EXERCÍCIO 1
# Jeito 1
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0
for i in range(len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print(pares)
print(impares)
# Jeito 2
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0
for i in lista_numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(pares)
print(impares)
-----------------------------------
# EXERCÍCIO 2
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for i in range(len(lista_numeros)):
    soma += lista_numeros[i]
print(soma)
-----------------------------------
# EXERCÍCIO 3
lista_profs = ['Lucas', 'Lucas D.', 'Ana', 'Danilo', 'Caio']
for i in range(len(lista_profs)):
    if 'Danilo' == lista_profs[i]:
        print(f'Danilo foi encontrado na posição {lista_profs[i]}, ele é muito querido!')
if 'Danilo' not in lista_profs:
    print('Danilo não está na lista :(')
-----------------------------------
# EXERCÍCIO 4
lista_profs = ['Lucas', 'Lucas D.', 'Ana', 'Danilo', 'Caio']
materias = ['Front-End', 'Edge', 'Storytelling', 'Python', 'Web Development']
for i in range(len(lista_profs)):
    print(f'O/A prof {lista_profs[i]} dá aula de {materias[i]}')
-----------------------------------
# EXERCÍCIO 5
lista = []
for i in range(4):
    num = input(f'Diga o {i+1}° número: ')
    while not num.isnumeric():
        print('Deve ser um número inteiro!')
        num = input(f'Diga o {i+1}° número: ')
    num = int(num)
    lista.append(num)
    print(lista)
-----------------------------------
lista = [1, 20, 30, 17, 333, 8, 2]
maior = lista[0]
for i in range(1, len(lista)):
    print(f'Vou testar se {lista[i]} é maior que {maior}')
    if lista[i] > maior:
        print('É maior, vou trocar')
        maior = lista[i]
        indice = i
        # posicao = lista.index(maior)
print()
print(f'Maior número: {maior}\nÍndice do maior número: {indice}')
'''