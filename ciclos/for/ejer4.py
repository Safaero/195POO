altura = int(input("Ingrese la altura del triángulo (un número entero): "))

for i in range(1, altura + 1):
    for j in range(i):
        print("$", end="")
    print()
