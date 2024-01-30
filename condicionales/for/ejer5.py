palabra = input("ingrese una palabra:")
letra = input("ingrese la letra:")
letra_contador = 0
for letra in palabra:
    if letra.lower() in (letra):
     letra_contador += 1 
print(f"la palabra ' {palabra}' tiene la letra {letra_contador} veces .")