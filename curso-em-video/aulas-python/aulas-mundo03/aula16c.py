# TUPLAS SÃO IMUTÁVEIS
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))   # Transforma em lista para 'printar'
print(lanche)           # Continua com a mesma ordem (IMUTÁVEL)

# Tuplas númericas
a = (2, 5, 4)
b = (5, 8, 9, 3, 1, 5, 2)
c = a + b
print(c)
print(f'A tupla \'c\' tem tamanho = {len(c)}')
print(f'Existem {c.count(5)} números \'5\' na tupla \'c\'')  # Quantos '5' existem na tupla?
print(f'O \'9\' está na posição {c.index(9)}')  # Em que posição está o '9'?

# Tuplas e tipos de dado
pessoa = ('Matheus', 20, 'M', 65.15, 'Sim')
print(pessoa)
del pessoa  # PODE-SE DELETAR UMA TUPLA!
print(pessoa)
