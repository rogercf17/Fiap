lado1 = int(input('Digite o valor do 1° lado do triângulo: '))
lado2 = int(input('Digite o valor do 2° lado do triângulo: '))
lado3 = int(input('Digite o valor do 3° lado do triângulo: '))
if lado1 == lado2 and lado1 == lado3 and lado3 == lado2:
    print('Este é um triângulo equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
    print('Este é um triângulo isósceles.')
elif lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
    print('Este é um triângulo escaleno.')
else:
    print('Falha!')