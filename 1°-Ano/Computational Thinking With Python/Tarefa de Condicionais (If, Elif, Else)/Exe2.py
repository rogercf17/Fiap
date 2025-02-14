ano_nascimento = int(input('Digite o ano de seu nascimento: '))

idade_votar = 2024 - ano_nascimento

if idade_votar >= 18:
    print('Você pode votar nestas próximas eleições')
else:
    print('Você não poderá votar nestas próximas eleições')