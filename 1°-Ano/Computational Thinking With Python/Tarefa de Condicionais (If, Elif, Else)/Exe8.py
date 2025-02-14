#Exercício com calculo de área
'''num_lados = int(input('Digite o número de lados do polígono: '))
if num_lados < 3:
    print('Não é um polígono.')
elif num_lados == 3:
    print('É um triângulo.')
    base = int(input('Digite o valor em metros da base do triângulo: '))
    altura = int(input('Digite o valor em metros da altura do triângulo: '))
    area = (base*altura) / 2
    print(f'A área do triângulo é {area} metros quadrados.')
elif num_lados == 4:
    print('É um quadrado.')
    lado = int(input('Digite o valor em metros do lado do quadrado: '))
    area = lado ** 2
    print(f'A área do quadrado é {area} metros quadrados.')
elif num_lados == 5:
    print('é um pentágono.')
else:
    print('Polígono não identificado.')'''

#Exercício com calculo de perímetro
num_lados = int(input('Digite o número de lados do polígono: '))
if num_lados < 3:
    print('Não é um polígono')
elif num_lados > 5:
    print('Polígono não identificado')
else:
    medida = int(input('Diga o tamanho do lado: '))
    if num_lados == 3:
        forma = 'Triângulo'
    elif num_lados == 4:
        forma = 'Quadrado'
    else:
        forma = 'Pentágono'
    perimetro = num_lados*medida
    print(f'Você escolheu o {forma} com perímetro de {perimetro}')
