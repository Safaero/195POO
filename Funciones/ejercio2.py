def area_circulo(radio):
    return 3.14*radio**2
def main():
    radio_circulo=float(input("ingrese radio:"))
    area_r = area_circulo(radio_circulo)
    print("area del circulo es igual:{area_r}")
main()
def volumen (radio,altura):
    return 3.14*radio**2*altura
def main():
    radio=float(input("ingrese radio cilindro"))
    altura=float(input("ingresar altura"))
    print(f"el volumen del cilindro es:{volumen(radio,altura)}")
main()