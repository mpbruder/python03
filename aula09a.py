frase = 'Curso em Video Python'


# Split - MUITO IMPORTANTE
dividido = frase.split()
for x in dividido:
    print('Dividido[{}]'.format(x))

# Letra dentro de um split
print(dividido[3][:2])

# Frase completa
print(frase)

# Somente o terceiro caractere
print(frase[3])

# Do terceiro ao decimo segundo caractere (o decimo terceiro fica de fora)
print(frase[3:13])

# Do inicio ao quinto caractere
print(frase[:6])

# Do decimo quinto ao ultimo caractere
print(frase[15:])

# Frase completa pulando de 2 e 2 caracteres
print(frase[::2])

# Tamanho
print(len(frase))

# Trocar
print(frase.replace('Python', 'Android'))

# Condição de busca
print('Curso' in frase)


# Texto grande, basta utilizar 3 aspas duplas
print("""\n\n\nA amizade consegue ser tão complexa...
Deixa uns desanimados, outros bem felizes...
É a alimentação dos fracos
É o reino dos fortes

Faz-nos cometer erros
Os fracos deixam se ir abaixo
Os fortes erguem sempre a cabeça
os assim assim assumem-os

Sem pensar conquistamos
O mundo geral
e construímos o nosso pequeno lugar
deixando brilhar cada estrelinha

Estrelinhas...
Doces, sensíveis, frias, ternurentas...
Mas sempre presentes em qualquer parte
Os donos da amizade...""")


