# Variavel Simples
lanche = 'Hamburger'
print(lanche)

# Varialvel composta
lanche1 = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche1)

print(lanche1[1])    # Segundo Elemento = Suco
print(lanche1[-1])   # Ultimo Elemento = Pudim
print(lanche1[-2])   # Penultimo elemento = Pizza
print(lanche1[0:3])  # Primeiro até PUNULTIMO elemento
print(lanche1[:2])   # Primeiro elemento até o elemento (2-1)
print(lanche1[-3:3]) # LOUCURA!

# Uso do FOR com variáveis compostas
for comida in lanche1:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche1):
    print(f'Eu vou comer {comida} na posição {pos}')

'''
    Variaveis compostas:
        lanche = ()             - Tupla: SÃO IMUTÁVEIS!!!
        lanche = []             - Lista
        lanche = {}             - Dicionário
'''
