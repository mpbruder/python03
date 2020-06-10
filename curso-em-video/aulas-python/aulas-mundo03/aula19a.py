# Declaração Dicionário
pessoas = {'nome': 'Matheus', 'idade': 22, 'sexo': 'M'}

# Prints
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# Print extras
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

# Laços
print('\n\nLAÇOS')
for k, v in pessoas.items():
    print(f'{k} é {v}')

print()

for i in pessoas.values():  # pessoas.keys() - Funciona igual
    print(i)
