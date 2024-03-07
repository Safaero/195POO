import tkinter as tk
from tkinter import messagebox

def submit(persona1, name_entry, password_entry):
    nombre = name_entry.get()
    clave = password_entry.get()

    if nombre == '' or clave == '':
        messagebox.showerror("Error", "ingresar algo")
        return

    if persona1.validar(nombre, clave): 
        messagebox.showinfo("acceso concedido", "sea bienvenido, " + nombre)
    else:
        messagebox.showerror("error", "user o contraseña equivocados")

def mostrar_ventana_login(persona1):
    root = tk.Tk()
    root.title("ingreso de nombre y nlave")

    name_label = tk.Label(root, text="Nombre:")
    name_label.grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(root, text="Clave:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    submit_button = tk.Button(root, text="Enviar", command=lambda: submit(persona1, name_entry, password_entry))
    submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
