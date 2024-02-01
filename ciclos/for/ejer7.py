tamaño_base = int(input("tamaño de base?"))

for i in range(1, tamaño_base + 1, 2):
    print(" " * ((tamaño_base - i) // 2) + "*" * i)
