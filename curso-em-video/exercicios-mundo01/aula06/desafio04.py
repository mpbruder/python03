var = input('Digite algo: ')

print('Tipo primitivo: {}\n'.format(type(var)))

print('É int? {}'.format(var.isnumeric()))
print('É str? {}'.format(var.isalpha()))
print('É float? {}'.format(var.isdecimal()))
print('É alfanumerico? {}'.format(var.isalnum()))
print('É ASCII? {}'.format(var.isascii()))
print('É printavel? {}'.format(var.isprintable()))
print('É maiusculo? {}'.format(var.isupper()))
