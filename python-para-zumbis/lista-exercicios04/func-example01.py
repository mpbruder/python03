def fat(x):
    fat = k = 1
    for i in range(k, x + 1):  # +1 devido condição de parada
        fat = fat * i
    return fat
