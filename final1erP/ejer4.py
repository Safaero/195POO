numero = input("numero de 3 digitos: ")

while len(numero) != 3 or not numero.isdigit():
    numero = input("numero que tenga 3 digitos: ")

sumatotal = sum(int(digitos) for digitos in numero)

print(f"la suma de los numeros {numero} es iguala: {sumatotal}")