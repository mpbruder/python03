nome = str(input('Digite seu nome completo: ')).strip()
# Todas letras maiusculas
print(nome.upper())

# Todas Letras Minusculas
print(nome.lower())

# Total de letras sem considerar espaços
caracteres = len(nome)
espacos = int(nome.count(' '))
letras = caracteres - espacos
print('Existem {} letras ao total.'.format(letras))

# Total de letras do primeiro nome
divido = nome.split()
fname = divido[0]
print('Primeiro nome possui {} letras.'.format(len(fname)))
