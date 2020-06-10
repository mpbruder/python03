import math
ang = int(input('Digite um angulo: '))

# Comando 'radians(x)' converte graus em radianos!
rad = math.radians(ang)
# Comando 'degrees(x)' faz o contrário!

print('O angulo {} tem como caracteristica:'.format(rad))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(math.sin(rad), math.cos(rad), math.tan(rad)))
