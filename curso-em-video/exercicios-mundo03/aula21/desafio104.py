def leiaInt(texto):
    """
    Função que somente lê número inteiro.
    :param texto: Valor que será submetido à validação
    :return: Valor númerico inteiro
    """
    from cor import cores
    while True:
        valor = input(texto).strip()
        if not valor.strip().isnumeric():
            print(f'{cores["vermelho"]}ERRO! Digite um número inteiro.{cores["limpa"]}')
        else:
            return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
