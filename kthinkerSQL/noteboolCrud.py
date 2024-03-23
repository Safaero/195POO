from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

# Crear la ventana
Ventana = Tk()
Ventana.title("CRUD USUARIOS")
Ventana.geometry("500x300")

# Preparar el notebook para pestañas
panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

# Definir las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

# Agregar las pestañas
panel.add(pestana1, text="Crear usuario")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar usuario")
panel.add(pestana4, text="Editar usuario")
panel.add(pestana5, text="Eliminar usuario")

# Pestaña 1 formulario de insertar
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

Ventana.mainloop()
