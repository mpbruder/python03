from math import pow
print('*' * 20)
print(' CALCULADORA DE IMC')
print('*' * 20)
peso = float(input('Informe o peso (Ex. 65.6): '))
altura = float(input('Informe o altura (Ex. 1.70): '))

IMC = peso / pow(altura, 2)
print('\nResuldado IMC: {:.2f}'.format(IMC))

if IMC < 18.5:
    print('CUIDADO! Abaixo do peso')
elif IMC < 25:
    print('PARABÉNS! Peso ideal')
elif IMC < 30:
    print('CUIDADO! Sobrepeso')
elif IMC < 40:
    print('MUITO CUIDADO! Obesidade')
else:
    print('\nRISCO DE VIDA! Obesidade Mórbida')
