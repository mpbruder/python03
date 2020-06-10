def notas(* valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: Uma ou mais notas do alunos, aceita várias.
    :param sit: (Opcional), indica se deve ou não acrescentar uma situação.
    :return: Um dicionáro com várias informações sobre o aluno
    """
    dicionario = dict()

    maior = menor = cont = 0
    for num in valores:

        if cont == 0:
            maior = menor = num
            cont += 1
        else:
            if maior < num:
                maior = num
            if menor > num:
                menor = num

    dicionario['total'] = len(valores)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['média'] = (sum(valores) / len(valores))
    if sit:
        if dicionario['média'] < 6:
            dicionario['situação'] = 'RUIM'
        elif 6 <= dicionario['média'] < 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'BOA'

    return dicionario


# Programa Principal
resp = notas(5.5, 9, 10, 6.5)
print('-' * 30)
print(resp)

help(notas)
