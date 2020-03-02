valores = list()
for cont in range(0, 3):
    valor = int(input('Digite um valor para colocar na lista: '))
    valores.append(valor)
    
for ixd, v in enumerate(valores):
    print(f'Na posição {ixd} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
