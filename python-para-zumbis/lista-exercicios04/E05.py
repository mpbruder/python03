'''
Exercício 05 - Python para Zumbis
-------------
Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres.
Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
'''


def check_word(word, group):
    """
    Função que verifica se algum caractere de um determinado grupo está contido em uma dada palavra.
    :param word: palavra que deseja passar
    :param group: conjunto de caracteres que deseja saber se contem na palavra ('word')
    :return: Boolean relativo à presença ou nao dos caracteres 'group' na palavra 'word'
    """
    for i in word:
        if i in group:
            return True
    return False


texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
			Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up 
			to these principles. We want our community to be more diverse: whoever you are, and whatever your background, 
			we welcome you.'''

for k in '.,:':
    texto = texto.replace(k, ' ')

texto = texto.split()

lista = []
# cada palavra do texto "splitado"
for i in texto:
    # palavra tem 5 caractere?
    # Existe alguma letra na palavra contido no conjunto 'python'?
    if (len(i) > 4) and (check_word(i.lower(), 'python')):
        lista.append(i)

print(f'{lista}\n\nQntd. palavras: {len(lista)}')
