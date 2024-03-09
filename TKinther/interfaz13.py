import tkinter as tk
from tkinter import messagebox
from Clase13 import GeneradorContraseña
class InterfazGenerador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("generaor de contraseñas :)")

        self.longitud_var = tk.IntVar(value=8)
        self.CaracteresVar = tk.BooleanVar(value=False)

        tk.Label(self.ventana, text="longitud??").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.longitud_var)
        self.entry_longitud.pack()

        tk.Checkbutton(self.ventana, text="quiere caracteres especiales??", variable=self.CaracteresVar).pack()

        self.boton_generar = tk.Button(self.ventana, text="Generar Contraseña", command=self.generar_contraseña)
        self.boton_generar.pack()

        tk.Label(self.ventana, text="Contraseña generada:").pack()
        self.entry_contraseña = tk.Entry(self.ventana)
        self.entry_contraseña.pack()

        self.boton_comprobar = tk.Button(self.ventana, text="Comprobar Fortaleza", command=self.comprobar_fortaleza)
        self.boton_comprobar.pack()

    def generar_contraseña(self):
        longitud = self.longitud_var.get()
        especialesCar = self.CaracteresVar.get()

        generador = GeneradorContraseña()
        contraseña = generador.generar_contraseña(longitud, especialesCar)

        self.entry_contraseña.delete(0, tk.END)
        self.entry_contraseña.insert(0, contraseña)

    def comprobar_fortaleza(self):
        contraseña = self.entry_contraseña.get()
        longitud = len(contraseña)
        contiene_numeros = any(char.isdigit() for char in contraseña)
        contiene_especiales = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?`~" for char in contraseña)

        fortaleza = 0
        if longitud >= 11:
            fortaleza += 1
        if contiene_numeros:
            fortaleza += 1
        if contiene_especiales:
            fortaleza += 1

        messagebox.showinfo("fortaleza de contraseña", f"la fortaleza de la contraseña es: {fortaleza}/3")

ventana = tk.Tk()
app = InterfazGenerador(ventana)
ventana.mainloop()
