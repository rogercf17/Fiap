nome = input('Qual o seu nome? ')
while len(nome) <= 3:
    print('Nome inválido! Digite um nome com mais de 3 letras.')
    nome = input('Qual o seu nome? ')
idade = int(input('Quantos anos você têm? '))
while idade < 1 or idade > 150:
    print('Idade inválida! Digite uma idade entre 1 e 150.')
    idade = int(input('Quantos anos você têm? '))
salario = input('Qual o seu sálario bruto? ')
while not salario.isnumeric():
    print('Salário inválido! Digite um salário superior a R$ 0.')
    salario = int(input('Qual o seu sálario bruto? '))
sexo = input('Qual é teu sexo biológico? ')
while sexo != 'feminino' and sexo != 'masculino':
    print('Sexo biológico inválido! Digite masculino ou feminino.')
    sexo = input('Qual é teu sexo biológico? ')
est_civil = input('Qual o teu estado cívil? ')
while not(est_civil == 'solteiro' or est_civil == 'casado' or est_civil == 'viuvo' or est_civil == 'divorciado'):
    print('Estado cívil inválido! Digite solteiro ou casado ou viuvo ou divorciado.')
    est_civil = input('Qual o teu estado cívil? ')
print(f'Dados -\nNome: {nome}\nIdade: {idade}\nSalário: R$ {salario:.2f}\nSexo: {sexo}\nEstado Cívil: {est_civil}')