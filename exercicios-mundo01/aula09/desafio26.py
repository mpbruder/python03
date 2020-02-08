frase = str(input('Digite uma frase: ')).strip().upper()

# Quantas letras 'A' possui na frase?
print('Letra \'a\' aparece {} na frase.'.format(frase.count('A')))

# Posição da primeira aparição de 'A':
print('Primeira letra \'a\' aparece na posição {}.'.format(frase.find('A') + 1))

# Posição da ultima letra 'A':
print('Ultima letra \'a\' aparece na posição {}.'.format(frase.rfind('A') + 1))
