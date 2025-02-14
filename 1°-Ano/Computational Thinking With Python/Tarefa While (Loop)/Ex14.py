intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
qntd = int(input('Quantos números deseja digitar? '))
i = 0
while i < qntd:
    num = int(input('Digite um número: '))
    if num > 0 and num <= 25:
        intervalo1 += 1
    elif num <= 50:
        intervalo2 += 1
    elif num <= 75:
        intervalo3 += 1
    else:
        intervalo4 += 1
    i += 1
print(f'Intervalo [0-25] têm: {intervalo1} números\n Intervalo [26-50] têm: {intervalo2} números\nIntervalo [51-75] têm: {intervalo3} números\nIntervalo [76-100] têm: {intervalo4} números')