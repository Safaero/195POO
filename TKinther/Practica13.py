from interfaz13 import mostrar_ventana_login
class cont:
    
    def __init__(self):
        self.__List = []
     
        while True:
            opcion = input(" 1 para agregar la longitud de la contraseña o caracteres especiales")
            
            if opcion == "1":
                print("Largo de contraseña y si quiere incluir caracteres especiales ")
                long = input("largo:")
                clave = input("Desea agregar caracteres especiales: ")
                self.insertar(len(self.__List) + 1, long, clave)
            elif opcion == "2":
                mostrar_ventana_login(self)
            else:
                break
     
