def contador(* num):
    print(f'Valores recebidos foram {num}, totalizando {len(num)} números. ')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# Programa principal

# Trabalhando com PACOTES
contador(2, 3, 5, 4)
contador(4, 5, 1, 0)
contador(0, 1)
contador(1, 2, 3)

# Trabalhando com LISTAS
valores = [5, 2, 4, 6]
print(f"Lista de valores = {valores}")
dobra(valores)
print(f"Lista do dobro de valores = {valores}")

