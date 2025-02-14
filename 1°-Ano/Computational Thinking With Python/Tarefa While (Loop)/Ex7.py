'''
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
i = num1 + 1
while i < num2:
    print(i, end = ' ')
    i += 1
num = 1
while num <= 10:
    i = 1
    print(f'Tabuada do {num}')
    while i <= 10:
        print(f'{num} x {i} = {num*i}')
        i += 1
    num += 1
    print('\n')
'''
i = 1
num = int(input('Digite um número para ser feito sua tabuada: '))
print(f'Tabuado do {num}')
while i <= 10:
    print(f'{num} x {i} = {num*i}')
    i += 1