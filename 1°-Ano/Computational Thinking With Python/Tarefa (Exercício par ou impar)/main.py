'''
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} é par!')
else:
    print(f'{num} é ímpar!')
'''
'''
#Sem laço de repetição
par = 0
impar = 0
n1 = int(input('Digite o 1° número: '))
if n1%2==0:
    par = 1
else:
    impar = 1
n2 = int(input('Digite o 2° número'))
if n2%2==0:
    par = par + 1
else:
    impar = impar + 1
n3 = int(input('Digite o 3° número'))
if n3%2==0:
    par = par + 1
else:
    impar = impar + 1
n4 = int(input('Digite o 4° número'))
if n4%2==0:
    par = par + 1
else:
    impar = impar + 1
n5 = int(input('Digite o 5° número'))
if n5%2==0:
    par = par + 1
else:
    impar = impar + 1
print(f'Quantidade de pares = {par}\nQuantidade de ímpares = {impar}')
'''
#Com laço de repetição
q = 0
par = 0
impar = 0
while q < 5:
    n = int(input(f'Digite o {q+1}° número: '))
    if n%2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    q += 1
print(f'Quantidade de pares = {par}\nQuantidade de ímpares = {impar}')