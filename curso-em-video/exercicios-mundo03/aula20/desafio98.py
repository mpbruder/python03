from time import sleep


def contador(ini, fim, passo):
    print('-=' * 30)
    if passo == 0:
        passo = 1
    passo = abs(passo)  # Manter o valor do passo constante
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    sleep(2)

    # Verificar se o passo é positivo ou negativo
    if ini <= fim:
        aux = 1
    else:
        aux = -1
        passo *= -1

    # Escrever a sequencia na tela
    for c in range(ini, fim + aux, passo):
        print(c, end=' ', flush=True)
        sleep(0.45)
    print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Personalize a contagem!')
i = int(input(f'{"Inicio:":8}'))
f = int(input(f'{"Fim:":8}'))
p = int(input(f'{"Passo:":8}'))
contador(i, f, p)
