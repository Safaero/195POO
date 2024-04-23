numeros = []
for i in range(10):
    numero = int(input("ingresa numeros: "))
    numeros.append(numero)
    

opcion = int(input("elegir opcion:\n1. mostrar lista invertida \n2. lista sin repetidos\n"))


if opcion == 1:
    print("numeros invertidos:")
    print(numeros[::-1])
        
elif opcion == 2:
    numeros_sin_repetir = list(set(numeros))
    print("sin repetidos:")
    print(numeros_sin_repetir)
    
else:
    print("por favor elige 1 o 2.") 