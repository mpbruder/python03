from time import sleep


def maior(* valores):
    bigger = cont = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    print(f'{valores} → Totalizando {len(valores)} valores.')
    for num in valores:
        if cont == 0:
            bigger = num
            cont += 1
        else:
            if bigger < num:
                bigger = num
    print(f'O maior valor informado foi {bigger}')
    sleep(1)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
