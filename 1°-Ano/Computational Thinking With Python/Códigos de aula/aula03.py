'''v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
v3 = int(input('Digite o 3° valor: '))
if v1 == v2 or v1 == v3 or v2 == v3:
    print('Alguns dos valores são iguais. Digite números diferentes!')
else:
    if v1 > v2 > v3:
        print(f'A ordem crescente é: {v3}-{v2}-{v1}')
    elif v1 > v3 > v2:
        print(f'A ordem crescente é: {v2}-{v3}-{v1}')
    elif v2 > v1 > v3:
        print(f'A ordem crescente é: {v3}-{v1}-{v2}')
    elif v2 > v3 > v1:
        print(f'A ordem crescente é: {v1}-{v3}-{v2}')
    elif v3 > v1 > v2:
        print(f'A ordem crescente é: {v2}-{v1}-{v3}')
    elif v3 > v2 > v1:
        print(f'A ordem crescente é: {v1}-{v2}-{v3}')'''
'''v1 = int(input('Digite o 1° valor'))
v2 = int(input('Digite o 2° valor'))
v3 = int(input('Digite o 3° valor'))
if v1 > v2 and v1 > v3:
    if v2 > v3:
        print(f'Ordem crescente: {v3}-{v2}-{v1}')
    else:
        print(f'Ordem crescente: {v2}-{v3}-{v1}')
elif v2 > v3 and v2 > v1:
    if v1 > v3:
        print(f'Ordem crescente: {v3}-{v1}-{v2}')
    else:
        print(f'Ordem crescente: {v1}-{v3}-{v2}')
else:
    if v1 > v2:
        print(f'Ordem crescente: {v2}-{v1}-{v3}')
    else:
        print(f'Ordem crescente: {v1}-{v2}-{v3}')'''
'''v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
v3 = int(input('Digite o 3° valor: '))
if v1 == v2 or v1 == v3 or v2 == v3:
    print('Alguns dos valores são iguais. Digite números diferentes!')
else:
    if v1 > v2:
        v1, v2 = v2, v1
    if v2 > v3:
        v2, v3 = v3, v2
    if v1 > v2:
        v1, v2 = v2, v1
    print(f'A ordem crescente é: {v1}-{v2}-{v3}')
'''
'''a = int(input('Digite o valor 1: '))
b = int(input('Digite o valor 2: '))
c = int(input('Digite o valor 3: '))
if a > b and a > c:
    aux = a
    a = c
    c = aux
elif b > c:
    aux = b
    b = c
    c = aux
if a > b:
    aux = a
    a = b
    b = aux
print(a,b,c)'''