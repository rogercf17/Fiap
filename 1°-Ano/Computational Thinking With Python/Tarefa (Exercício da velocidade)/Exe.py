v = int(input('Digite a velocidade do automóvel: ')) #Variável de velocidade
if v <= 100:
    multa = 0
elif v <= 120:
    multa = v * 0.2
elif v <= 150:
    multa = 24 + (0.3 * v)
else:
    multa = 69 + (0.4 * v)
print(f'O automóvel atingiu a velocidade de {v} km/h, e terá que pagar uma multa de R$ {multa}')