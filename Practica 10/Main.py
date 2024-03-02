import sys
from Persona import *

objectPeople= Persona()

while True:
    print("==menu==")
    print("1.insertar persona:")
    print("2 consultar:")
    print("buscar una persona 3")
    print("editar persona 5:")
    print("salir: 6")
    opcion = input("Elige una opcion:")
    
    if opcion == "1":
        print("==ingresar los datos del usuario")
        id = input ("Escribir el id:")
        nom= input("escribir nombre")
        eda= input("escribit edad:")
        
        objectPeople.Insertar(id,nom,eda)
        print(":: Persona agregada correctamente ::")
        
    elif opcion == "2":
        print("::estos son las perosnas guaradas::")
        objectPeople.consultarTodos()
        
    elif opcion == "3":
        print("::introducir id de la persona::")
        id= input("id:")
        objectPeople.buscarUsuario(id)
        
    elif opcion == "4":
        print("::introducir id de la persona a eliminar::")
        id= input ("ID:")
        objectPeople.eliminar(id)
        
        