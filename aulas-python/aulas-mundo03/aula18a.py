# Declarações das listas
dados = list()
pessoas = list()

dados.append('Matheus')
dados.append(20)
pessoas.append(dados[:])  # Cria apenas uma cópia

dados[0] = 'Nicolli'
dados[1] = 19
pessoas.append(dados[:])  # Cria apenas uma cópia

# Mostrar as execuções
print(f'Lista \'pessoas\': {pessoas}')  # Simples, todas pessoas
print(pessoas[0][0])  # Composta
print(pessoas[1][0])
print(pessoas[0][1])

# Mostrar todos os dados formatados!
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos.')
