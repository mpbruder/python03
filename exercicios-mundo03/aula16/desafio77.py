palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')

# 'palavra' é cada palavra dentro da tupla
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos: ', end='')
    # 'letra' é cada letra dentro da palavra (cada palavra é uma numeros de caracteres)
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
    print('', end='\n')
