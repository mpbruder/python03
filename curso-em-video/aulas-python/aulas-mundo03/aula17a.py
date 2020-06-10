num = [0, 5, 6, 2, 2]
print(f'Lista: {num}')

# Modificar um elemento
num[1] = 7
print(f'Lista modificada: {num}')

# Adicionar um elemento
# num[4] = 5  # ERRO! Não existe o elemento de indice 4, só de 0 a 3
# Append - inserir no final
num.append(2)
print(f'Usando método \'append\': {num}')

# Insert - inserir em qualquer posição
num.insert(0, 99)
print(f'Usando método \'insert\': {num}')
num.insert(2, 98)
print(f'Usando método \'insert\': {num}')

# Remover um elemento
num.pop()  # Elimina o ultimo da lista
print(f'Usando método \'pop()\': {num}')
num.pop(1)
print(f'Usando método \'pop(1)\': {num}')
del num[0]
print(f'Usando método \'del num[0]\': {num}')
# Impedir que um objeto inexistente seja removido!
if 2 in num:
    num.remove(2)
print(f'Usando método \'remove(objeto)\': {num}')

'''
    Variaveis compostas:
        lanche = ()             - Tupla: SÃO IMUTÁVEIS!!!
        lanche = []             - Lista: SÃO MUTÁVEIS!!!
        lanche = {}             - Dicionário
'''
