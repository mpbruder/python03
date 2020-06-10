from datetime import date
atual = date.today().year
# Não altere esse valor, é uma constante.
limite = 7

# Inicialização da variável soma
maiores = 0

for c in range(0, limite):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c + 1)))
    idade = atual - nasc
    if idade >= 18:
        maiores += 1

menores = limite - maiores
print('\n{} Pessoas com idade SUPERIOR a 18 anos\n{} Pessoas com idade INFERIOR a 18 anos.'.format(maiores, menores))
