salario = int(input('Digite seu salário: '))
aumento = 1.5/100
salario += (salario * aumento)
contador = 1995
final_contador = 2005
while contador <= final_contador:
    salario *= (1+aumento)
    aumento *= 2
    contador += 1
print(f'Seu salário com o aumento será de R$ {salario:.2f}')