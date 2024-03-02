from A import *

#lista para almacenar registro de usuarios
usuarios = []
#guardar datos de la persona

print("ingresar datos de la persona")

nombre= input("ingresar nombre")
correo= input("ingresar correo de la persona")
contra= input("ingresar contraseña")
id= input(int("ingresar id usuario"))
apep= input("apellido paterno")
apem= input("apellido materno")

#crear objeto a partir de los atributos

Save = User(nombre,correo,contra,id,apep,apem)
Save.append(Save)
#consulta de user 

for user in Save:
    print(User.getnombre())
    print(User.getcorreo())
    print(User.getcontra())
    print(User.getid())
    print(User.getapep())
    print(User.getapem())
    print()
    

#editar User

Edit = input("Nombre del nuevo user")
for User in Save:
    if User.getnombre() == Edit:
        nuevo_nombre = input ("nuevo nombre de usuario")
        User.setnombre(nuevo_nombre)

#borrar user

nombre_eliminar = input("nombre user a eliminar")
for User in Save:
    if User.getnombre() == nombre_eliminar:
        Save.eliminar(User)
        
