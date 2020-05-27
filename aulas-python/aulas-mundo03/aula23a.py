# try = Tente fazer isso...
try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    res = n / d
# except = Erro que pode acontecer no seu programa
except Exception as erro:
    print(f'Error: {erro.__class__}')
# else = ações que devem ocorrer quando não houver erro no programa
else:
    print(f'O resultado foi {res:.1f}')
# finnaly = ações que devem acontecer se houve erro OU não.
finally:
    print(f'Volte sempre!')
