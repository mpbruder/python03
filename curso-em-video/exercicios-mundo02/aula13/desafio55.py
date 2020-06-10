# Variáveis
pessoas = []
limite = 5

for c in range(0, limite):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c + 1)))
    pessoas.append(peso)  # Acrescentar ao vetor

# Ordenar o array
pessoas.sort()
print('\nMaior peso lido foi {:.1f}Kg.\nMenor peso lido foi {:.1f}Kg.'.format(pessoas[limite - 1], pessoas[0]))
