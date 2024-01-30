palabra = input("ingrese una palabra:")
contador_vocals = 0
for letra in palabra:
    if letra.lower() in "aieou":
     contador_vocals += 1 
print(f"la palabra ' {palabra}' tiene {contador_vocals} vocal(es).")