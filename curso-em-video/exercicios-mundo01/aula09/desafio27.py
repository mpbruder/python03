n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

# Primeiro nome
fname = nome[0]

# Ultimo nome
lname = nome[len(nome) - 1]

print('Primeiro nome: {}'.format(fname))
print('Último nome: {}'.format(lname))
