cidade = str(input('Em que cidade você nasceu? ')).strip()

# '[:5]' acha a string "SANTO" mesmo que nao seja uma palavra composta
if cidade[:5].lower() == 'santo':
    print('Yes! Começa com \'SANTO\'.')
else:
    print('Ops! Não começa com \'SANTO\'.')
