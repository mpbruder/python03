'''
Exercício 06 - Python para Zumbis
-------------
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 
'''
print('TEMPO DE VIAGEM')
dist = float(input('Distância (Km): '))
vel = float(input('Velocidade Média (Km/h): '))
print('=' * 25)
hora = dist // vel
minuto = (dist / vel - hora) * 60
print(hora)
print(int(minuto))
print(f'Tempo aprox. => {int(hora)} hora(s) e {int(minuto)} minuto(s)')
