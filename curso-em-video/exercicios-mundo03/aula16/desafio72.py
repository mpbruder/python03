numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    # Tratamento do programa, isto é, printar o número
    num = -1
    while num < 0 or num > 20:
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[num]}.\n')

    # Tratamento do encerramento do programa
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
