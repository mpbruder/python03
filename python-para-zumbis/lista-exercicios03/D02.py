'''
DESAFIO 02 - Python para Zumbis
-------------
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. 
Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos. 
Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
'''
conta = int(input('PAGAR (R$): '))
pagto = int(input('PAGO (R$): '))
if pagto > conta:
    notas = [50, 20, 10, 5, 2, 1]
    troco = pagto - conta
    for nota in notas:
        k = 0
        while troco >= nota:
            troco -= nota
            k += 1
        print(f'{k} notas de R${nota:^5}')
