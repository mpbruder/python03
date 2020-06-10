titulo = ' MERCADO MATHEUS '
barato = ' '
cont = totMaisBarato = totCompra = totMil = 0

print(f'{titulo:=^40}')

while True:
    # Ler dados do usuário
    prod = str(input('Nome Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    cont += 1

    # a) Total da compra
    totCompra += preco
    # b) Produtos preço > 1000
    if preco > 1000:
        totMil += 1
    # c) Produto mais barato
    if cont == 1 or preco < totMaisBarato:
        totMaisBarato = preco
        barato = prod

    # Ponto de decisão de parada
    print('-' * 30)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-' * 30)

    # STOP: Execução do Laço
    if opcao == 'N':
        break

print(f'{" Fim do Programa ":=^40}')
print(f'TOTAL DA COMPRA: R$ {totCompra:.2f}')
print(f'Produtos acima de R$ 1000: {totMil}')
print(f'Produto mais barato foi {barato} que custa R$ {totMaisBarato:.2f}')
