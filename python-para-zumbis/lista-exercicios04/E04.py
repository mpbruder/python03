'''
Exercício 04 - Python para Zumbis
-------------
Seja o statement sobre diversidade, gere uma lista de palavras deste texto com split(),
a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”.
Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''
texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone.
			Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up
			to these principles. We want our community to be more diverse: whoever you are, and whatever your background,
			we welcome you.'''

for k in '.,:':
    texto = texto.replace(k, ' ')

texto = texto.split()

lista = []
for i in texto:
    if (i[0].lower() in 'python') or (i[-1] in 'python'):
        lista.append(i)

print(f'{lista}')
