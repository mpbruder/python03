def voto(datanasc):
    """
    Função calcula a obrigatoriedade de voto de acordo com a data de nascimento.
    :param datanasc: Data de nascimento
    :return: Idade e obrigatoriedade de voto
    """
    from datetime import date  # Escopo de importação
    ano = date.today().year
    idade = ano - datanasc
    if idade < 16:
        condicao = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 60:
        condicao = 'VOTO OPICIONAL'
    else:
        condicao = 'VOTO OBRIGATÓRIO'

    # Retorno da função
    return f'Com {idade} anos: {condicao}'


# Programa Principal
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
