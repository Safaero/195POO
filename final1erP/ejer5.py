N = int(input("Ingrese la cantidad N de numeros: "))

numeros = []
for i in range(N):
    numero = int(input(f"ingrese numeros {i+1}: "))
    numeros.append(numero)

suma_pares = 0
suma_impares = 0

for num in numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

print(f" suma de pares: {suma_pares}")
print(f"suma de impares es: {suma_impares}")