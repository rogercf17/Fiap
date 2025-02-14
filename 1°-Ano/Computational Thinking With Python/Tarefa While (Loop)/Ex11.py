i = 1
divisivel = 0
numero = int(input('Digite um número: '))
while i <= numero:
    if numero % i == 0:
        divisivel += 1
    i += 1
if divisivel > 2:
    print(f'O número {numero} não é primo.')
else:
    print(f'O número {numero} é primo.')