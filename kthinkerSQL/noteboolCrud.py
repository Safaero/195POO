from tkinter import Tk, Label, Entry, Button, Text, ttk
import tkinter as tk
from Controlador import *

objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    
def busUsuario():
    usuarioBD = objControlador.buscarUsuario(varBus.get())

    resultado_texto.delete(1.0, tk.END)
    if usuarioBD:

        resultado_texto.insert(tk.END, usuarioBD)
    else:
        resultado_texto.insert(tk.END, "Usuario no encontrado")
        
def consultarTodos():
    usuarios = objControlador.consultarTodosUsuarios()

    resultado_texto_consulta.delete(1.0, tk.END)
    if usuarios:
        for usuario in usuarios:
            resultado_texto_consulta.insert(tk.END, f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}\n")
    else:
        resultado_texto_consulta.insert(tk.END, "no hay usuarios")

Ventana = Tk()
Ventana.title("CRUD USUARIOS")
Ventana.geometry("500x300")


panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")


pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

panel.add(pestana1, text="Crear usuario")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar usuario")
panel.add(pestana4, text="Editar usuario")
panel.add(pestana5, text="Eliminar usuario")

Label(pestana1, text="Registro de Usuario", fg="green", font=("New Times Roman", 18)).pack()

var1 = tk.StringVar()
Label(pestana1, text="nombre").pack()
Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(pestana1, text="correo:").pack()
Entry(pestana1, textvariable=var2).pack()

var3 = tk.StringVar()
Label(pestana1, text="contraseña:").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text="guardar usuario", command=ejecutaInsert).pack()

Label(pestana2, text="Buscar usuario por ID", fg="red", font=("New Times Roman", 18)).pack()

varBus = tk.StringVar()
Label(pestana2, text="ID:").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text="Buscar usuario", command=busUsuario).pack()

resultado_texto = Text(pestana2, height=5, width=52)
resultado_texto.pack()

Label(pestana3, text="Consulta de todos los usuarios", fg="blue", font=("New Times Roman", 18)).pack()

Button(pestana3, text="Actualizar", command=consultarTodos).pack()
resultado_texto_consulta = Text(pestana3, height=10, width=52)
resultado_texto_consulta.pack()
consultarTodos()
Ventana.mainloop()
