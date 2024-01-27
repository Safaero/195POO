edad_client = int(input("Introduce la edad del cliente "))
if edad_client < 4:
    precio_entrada = 0 
elif 4 <= edad_client <= 18:
    precio_entrada = 110
else:
    precio_entrada = 190

print(f"El precio de la entrada es: ${precio_entrada}")
