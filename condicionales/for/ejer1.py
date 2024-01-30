numeros = input("ingrese un numero entero:")
impares_numeros = 1
for impares in numeros:
    if numeros % 2 == 0:
        impares +=1 
print(f"el total de impares es ' {numeros}' tiene {impares_numeros} vocal(es).")