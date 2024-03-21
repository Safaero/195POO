from tkinter import *
from tkinter import ttk
import tkinter as tk

# 1 crear la ventana
Ventana= Tk()
Ventana.title("CRUD USUARIOS")
Ventana.geometry("500x300")

#2. preparar el notebook para pestañas
panel= ttk.Notebook(Ventana)
panel.pack(fill='both',expand="yes")

#3. definir las pestañas del notebook
pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)

#agregamos las pestañaas
panel.add(pestana1, text= "Crear usuario")
panel.add(pestana2, text= "Buscar usuario")
panel.add(pestana3, text= "Consultar usuariop")
panel.add(pestana4, text= "editar usuario")
panel.add(pestana5, text= "eliminar usuario")

#5. Pestaña 1 formulario de instert

Label(pestana1, text="Registro de Usuario" ,fg="green", font=("New Times Roman",18)).pack()

var1= tk.StringVar()
Label(pestana1, text="nombre").pack()
Entry(pestana1, textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1, text="correo:").pack()
Entry(pestana1, textvariable=var2).pack()

var3= tk.StringVar()
Label(pestana1, text="contraseña:").pack()
Entry(pestana1, textvariable=var3).pack()

var4= tk.StringVar()
Label(pestana1, text="correo:").pack()
Entry(pestana1, textvariable=var4).pack()

var4= tk.StringVar()
Label(pestana1, text="correo:").pack()
Entry(pestana1, textvariable=var4).pack()

var5= tk.StringVar()
Label(pestana1, text="correo:").pack()
Entry(pestana1, textvariable=var5).pack()

Ventana.mainloop()