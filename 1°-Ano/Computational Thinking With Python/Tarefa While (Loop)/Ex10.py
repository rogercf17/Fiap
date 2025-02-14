i = 1
num = int(input('Qual número que você deseja calcular o fatorial? '))
fatorial = num
while True:
    fatorial *= i
    i += 1
    if i == num:
        break
print(f'Fatorial de {num} é: {fatorial}')