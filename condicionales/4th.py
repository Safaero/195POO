palabra = str(input("Introduce palabra"))
text = palabra[::-1]
if text == palabra:
    print("tu palabra es palindromo") 
else:
    print("no es palindromo")
