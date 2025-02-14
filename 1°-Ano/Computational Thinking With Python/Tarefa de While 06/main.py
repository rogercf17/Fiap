resp = input('Você tem carteira de motorista? responda com "sim" ou "não": ')
while resp != 'sim' and resp != 'não':
    print('Responda novamente, com "sim" ou "não"')
    resp = input('Você tem carteira de motorista? responda com "sim" ou "não": ')
    if resp == 'sim' or resp == 'não':
        print('Resposta correta, obrigado!')
        if resp == 'sim':
            print('SIMMMMMM')
        else:
            print('NÃOOOOOO')