letra = input("Ingrese una letra: ")
frase = input("Ingrese una frase: ")
letra_contador = 0

for caracter in frase:
    if caracter.lower() == letra.lower():
        letra_contador += 1

print(f"La letra '{letra}' aparece {letra_contador} veces en la frase '{frase}'.")
