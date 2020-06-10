'''
Exercício 01 - Python para Zumbis
-------------
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
'''
a = int(input('1º Lado: '))
b = int(input('2º Lado: '))
c = int(input('3º Lado: '))
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    if a == b == c:
        print('Triângulo equilátero!')
    elif a == b or a == c or b == c:
        print('Triângulo isóceles!')
    else:
        print('Triângulo escaleno!')
else:
    print('Medidas informadas não formam um triângulo')
