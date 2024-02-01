numero = int(input("Ingrese un número entero: "))
impares_numeros = []

for i in range(numero, 0, -1):
    if i % 2 != 0:
        impares_numeros.append(str(i))

resultado = ", ".join(impares_numeros)
print(f"Los números impares hacia atrás desde {numero} son: {resultado}.")
