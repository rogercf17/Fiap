par = 0
i = 0
while i < 5:
    num = int(input(f'Digite o {i+1}° número: '))
    if num % 2 == 0:
        par += 1
    i += 1
print(f'Total de pares: {par}\nTotal de ímpares: {i - par}')