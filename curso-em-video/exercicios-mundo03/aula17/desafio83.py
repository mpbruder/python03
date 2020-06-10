pilha = []
expressao = str(input('Digite a expressão: ')).strip()
for i in expressao:
    if i == '(':
        pilha.append(i)
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(i)
            break

# 'not list()' Verifica se a numeros está vazia...
if not pilha:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
