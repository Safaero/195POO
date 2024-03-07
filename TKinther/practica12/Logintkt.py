import tkinter as tk
from tkinter import messagebox
from Persona import Persona

def submit():
    nombre = name_entry.get()
    clave = password_entry.get()

    if nombre == '' or clave == '':
        messagebox.showerror("Error", "Ingresar algo")
        return

    if persona1.validar(nombre, clave): 
        messagebox.showinfo("Acceso concedido", "Bienvenido, " + nombre)
    else:
        messagebox.showerror("Error", "Usuario o clave incorrectos")

persona1 = Persona()

root = tk.Tk()
root.title("Ingreso de Nombre y Clave")

name_label = tk.Label(root, text="Nombre:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Clave:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Enviar", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
