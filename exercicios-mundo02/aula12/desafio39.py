from datetime import date
sexo = str(input('Escolha o sexo:\n'
                 '\t[ F ] Feminino\n'
                 '\t[ M ] Masculino\n'
                 ': ')).strip().upper()
if sexo == 'F':
    print('O Alistamento é necessário apenas para o sexo masculino.')
else:
    nasc = int(input('Qual seu ano de nascimento? '))
    print('*' * 35)

    limite = int(18)
    atual = date.today().year
    idade = atual - nasc
    prazo = abs(limite - idade)
    previsao = atual + prazo
    excedente = atual - prazo

    print('\nVocê possui {} anos.'.format(idade))
    if idade < limite:
        print('Ainda deve se alistar daqui a {}, isto é, em {}.'.format(prazo, previsao))
    elif idade == limite:
        print('Aliste-se esse ano, pois, você completa 18 anos em {}.'.format(atual))
    else:
        print('Provavelmente você já se alistou em {}, há {} anos atrás.'.format(excedente, prazo))
