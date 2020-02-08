import math
cat1 = float(input('Digite o valor do cateto adjacente: '))
cat2 = float(input('Digite o valor do cateto oposto: '))

# hip = sqrt(pow(cat1, 2) + pow(cat2, 2))

hip = math.hypot(cat1, cat2)
print('O valor da hipotenusa é {:.2f}'.format(hip))
