#programa que calcula la suma de los numeros pares del 1 al 10
suma = 0
for num in range(1,11):
    if num % 2 == 0:
        suma += num
print(f"la suma de los pares es: {suma}")
     
    