numero= int (input("ingrese un numero entero positivo:"))
if numero <0:
    print("el numero que ingreso no es positivo")
else:
    cuenta_atras=",".join(map(str,range(numero,-1,-1)))
    print("la cuenta tras desde {numero} hasta 0 es: {cuenta_atras}.")