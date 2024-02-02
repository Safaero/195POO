def decimal_a_binario(numero):
    binario = bin(numero)[2:]
    return binario

def binario_a_decimal(binario):
    decimal = int(binario, 2) 
    return decimal

def main():
    opcion = input("Seleccione la operación 1 de decimal a binario presionar 2 para binario a decimal: ")

    if opcion == '1':
        numero_decimal = int(input("número decimal: "))
        resultado_binario = decimal_a_binario(numero_decimal)
        print(f"El binario es: {resultado_binario}")

    elif opcion == '2':
        numero_binario = input("el número binario: ")
        resultado_decimal = binario_a_decimal(numero_binario)
        print(f"decimal es: {resultado_decimal}")

    else:
        print("seleccione 1 o 2.")

main()
