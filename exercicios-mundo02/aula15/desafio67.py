titulo = ' PROGRAMA - TABUADA '

print('=' * 50)
print(f'{titulo:=^50}')
print('=' * 50, end='')

while True:
    num = int(input('\n\nQuer ver a tuabuada de qual valor? '))
    if num < 0:
        break
    # Laço com LIMITE que calcula tabuada.
    for i in range(0, 10):
        print(f'{num} x {i + 1:2} = {num * (i + 1):2}')

print('=' * 50)
print(f'{"PROGRAMA ENCERRADO. Volte Sempre!...":^50}')
print('=' * 50, end='')