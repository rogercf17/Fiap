angulo_1 = int(input('Digite o valor do 1° ângulo do triângulo: '))
angulo_2 = int(input('Digite o valor do 2° ângulo do triângulo: '))
angulo_3 = int(input('Digite o valor do 3° ângulo do triângulo: '))
if angulo_1 < 90 and angulo_2 < 90 and angulo_3 < 90:
    print('Este é um triângulo Acutângulo.')
elif angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
    print('Este é um triângulo reto.')
else:
    print('Este é um triângulo obtusângulo.')