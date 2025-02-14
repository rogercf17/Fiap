v1 = int(input('Digite o 1° valor: '))
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