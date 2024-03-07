class Persona:
    def __init__(self):
        self.__List = []

        while True:
            opcion = input("Presionar 1 para registrar usuario nuevo: ")

            if opcion == "1":
                print("Ingresar datos:")
                nomb = input("Nombre: ")
                clave = input("Clave del usuario: ")
                self.insertar(len(self.__List) + 1, nomb, clave)
            elif opcion =="2":
                print()
            else:
                break

    def insertar(self, id, nomb, clave):
        self.__List.append({"Id": id, "Nombre": nomb, "Clave": clave})

    def validar(self, nombre, clave):
        for persona in self.__List:
            if persona["Nombre"] == nombre and persona["Clave"] == clave:
                return True
        return False



persona1 = Persona()
