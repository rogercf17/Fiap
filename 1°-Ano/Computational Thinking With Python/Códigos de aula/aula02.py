'''
nome = input('Diga seu nome: ')
primeiro_num = int(input(f'{nome}, diga um número: '))
segundo_num = int(input(f'{nome}, diga um outro número: '))
soma = primeiro_num + segundo_num
sub = primeiro_num - segundo_num
div = primeiro_num / segundo_num
mult = primeiro_num * segundo_num
print(f'Soma = {soma}')
print(f'Subtração = {sub}')
print(f'Multiplicação = {mult}')
print(f'Divisão = {div}')
--------------------------------------------------------
nome = input('Diga seu nome: ')
frase = 'A '
frase = frase + nome
frase = frase + ' é lindinha'
frase = frase + ' demais!'
print(frase)
--------------------------------------------------------
inicio_frase = input('Inicie a frase: ')
final_frase = input('Termine a frase: ')
inicio_frase += ' ' + final_frase
print(inicio_frase)
--------------------------------------------------------
a = 2==3
print(a)
a = 2!=3
print(a)
a = 2<3
print(a)
a = 2>3
print(a)
a = 2>=3
print(a)
a = 2<=3
print(a)
--------------------------------------------------------
primeiro_num = 2
segundo_num = 3
a = primeiro_num==segundo_num
print(f'A comparação {primeiro_num} "==" {segundo_num} é {a}')
a = primeiro_num!=segundo_num
print(f'A comparação {primeiro_num} "!=" {segundo_num} é {a}')
a = primeiro_num<segundo_num
print(f'A comparação {primeiro_num} "<" {segundo_num} é {a}')
a = primeiro_num<=segundo_num
print(f'A comparação {primeiro_num} "<=" {segundo_num} é {a}')
a = primeiro_num>segundo_num
print(f'A comparação {primeiro_num} ">" {segundo_num} é {a}')
a = primeiro_num>=segundo_num
print(f'A comparação {primeiro_num} ">=" {segundo_num} é {a}')
--------------------------------------------------------
a = 2
b = 3
c = 4
d = 10
print(f'A comparação: {a}>{b} or {c}<{d} resulta em {a>b or c<d}')
print(f'A comparação: {a}<{b} or {c}>{d} resulta em {a>b or c<d}')
print(f'A comparação: {a}=={b} or {c}!={d} resulta em {a>b or c<d}')
print(f'A comparação: {a}!={b} or {c}=={d} resulta em {a>b or c<d}')
print(f'A comparação: {a}<={b} or {c}>={d} resulta em {a>b or c<d}')
print(f'A comparação: {a}>={b} or {c}<={d} resulta em {a>b or c<d}')
print(f'A comparação: {a}>{b} or {c}<{d} resulta em {a>b and c<d}')
print(f'A comparação: {a}<{b} or {c}>{d} resulta em {a>b and c<d}')
print(f'A comparação: {a}=={b} or {c}!={d} resulta em {a>b and c<d}')
print(f'A comparação: {a}!={b} or {c}=={d} resulta em {a>b and c<d}')
print(f'A comparação: {a}<={b} or {c}>={d} resulta em {a>b and c<d}')
print(f'A comparação: {a}>={b} or {c}<={d} resulta em {a>b and c<d}')
--------------------------------------------------------
senha_digitada = input('Digite sua senha: ')
senha_correta = '170105'
if senha_digitada == senha_correta:
    print('Senha digitada está correta!')
--------------------------------------------------------
idoso = input('Você é idoso? ')
cadeirante = input('Você é cadeirante? ')
if idoso == 'sim' or cadeirante == 'sim':
    print("Você pode estacionar nesta vaga preferencial")
--------------------------------------------------------
idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você não pode beber cachaça, que pena!')
--------------------------------------------------------
idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você não pode beber cachaça, que pena!')
else:
    print('Aeeeeee você pode beber, beba com moderação!')
--------------------------------------------------------  
letra = input('Digite uma letra: ')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'A letra "{letra}" é uma vogal')
else:
    print(f'A letra "{letra}" é uma consoante')
'''

'''
salario = float(input('Digite o seu salário: '))
if salario <= 1903.98:
    a = 0
    desconto = a * salario
    salario = salario - desconto
    print(f'Seu salário será de R$ {salario}')
elif salario <= 2826.65:
    a = 7.5 / 100
    desconto = a * salario
    salario = salario - desconto
    print(f'Seu salário será de R$ {salario}')
elif salario <= 3751.05:
    a = 15 / 100
    desconto = a * salario
    salario = salario - desconto
    print(f'Seu salário será de R$ {salario}')
elif salario <= 4664.68:
    a = 22.5 / 100
    desconto = a * salario
    salario = salario - desconto
    print(f'Seu salário será de R$ {salario}')
else:
    a = 27.5 / 100
    desconto = a * salario
    salario = salario - desconto
    print(f'Seu salário será de R$ {salario}')
------------------------------------------------------
salario = float(input('Digite o seu salário: '))
if salario <= 1903.98:
    a = 0
elif salario <= 2826.65:
    a = 7.5 / 100
elif salario <= 3751.05:
    a = 15 / 100
elif salario <= 4664.68:
    a = 22.5 / 100
else:
    a = 27.5 / 100
desconto = a * salario
salario -= desconto
print(f'Seu salário será de R$ {salario}')
'''