try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    res = n / d
except ZeroDivisionError:
    print(f'ERRO: Não existe divisão por zero.')
except KeyboardInterrupt:
    print(f'ERRO: Usuário não informou valores.')
except (ValueError, TypeError):
    print(f'ERRO: Tipo de dado incompatível.')
except Exception as erro:
    print(f'ERRO: {erro.__class__}')
else:
    print(f'Resultado:\n {n} ÷ {d} = {res}')
finally:
    print(f'\n=== Obrigado, volte sempre! ===')
