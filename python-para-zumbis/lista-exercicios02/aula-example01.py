vel = float(input('Velocidade (Km/h): '))
if vel > 110:
    multa = (vel - 110) * 5
    print(f'MULTADO! R$ {multa:.2f}')
else:
    print('Boa viagem!')
