altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo biológico: ')
if sexo == 'feminino' or sexo == 'Feminino':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Você é do sexo {sexo} e tem {altura:.2f} metros de altura, seu peso ideal é de {peso_ideal:.2f} quilos.')
elif sexo == 'masculino' or sexo == 'Masculino':
    peso_ideal = (72.7 * altura) - 58
    print(f'Você é do sexo {sexo} e tem {altura:.2f} metros de altura, seu peso ideal é de {peso_ideal:.2f} quilos.')
else:
    print('Informações inválidas, tente novamente.')