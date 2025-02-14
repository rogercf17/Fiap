def avaliar_condicoes_da_agua(ph, temperatura, salinidade):
    mensagem_problemas = []
    if 6.0 <= ph <= 8.0 and 25.0 <= temperatura <= 29.0 and 30.0 <= salinidade <= 35.0:
        return 'Condições ideias.'
    else:
        if ph < 6.0 or ph > 8.0:
            mensagem_problemas.append('pH fora dos limites ideais.')
        else:
            mensagem_problemas.append('pH dentro dos limites ideais.')
        if temperatura < 25.0 or temperatura > 29.0:
            mensagem_problemas.append('Temperatura fora dos limites ideais.')
        else:
            mensagem_problemas.append('Temperatura dentro dos limites ideais.')
        if salinidade < 30.0 or salinidade > 35.0:
            mensagem_problemas.append('Salinidade fora dos limites ideais.')
        else:
            mensagem_problemas.append('Salinidade dentro dos limites ideais.')
        return '\n'.join(mensagem_problemas)

def checa_numero(numero, mensagem):
    while not numero.isnumeric():
        print('Digite um valor inteiro positivo válido!')
        numero = input(mensagem)
    numero = float(numero)
    return numero

def questionario():
    ph = checa_numero(input('Digite o valor de pH: '), 'Digite o valor de pH: ')
    temperatura = checa_numero(input('Digite a temperatura (°C): '), 'Digite a temperatura (°C): ')
    salinidade = checa_numero(input('Digite o valor de salinidade (ppt): '),
                                    'Digite o valor de salinidade (ppt): ')
    resultado = avaliar_condicoes_da_agua(ph, temperatura, salinidade)
    print(f'Resultado da avaliação: \n{resultado}')

questionario()
