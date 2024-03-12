import tkinter as tk
from tkinter import messagebox
from Clase2 import GeneradorMatricula
class InterfazGenerador:
    
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Examen 2 :)")

        self.longitud_var = tk.IntVar(value='')
        self.CaracteresVar = tk.BooleanVar(value=False)

        tk.Label(self.ventana, text="Nombre:").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.longitud_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="Apellido paterno").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.longitud_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="Apellido materno").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.longitud_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="Año de nacimiento").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.longitud_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="carrera:").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.longitud_var)
        self.entry_longitud.pack()


        self.boton_generar = tk.Button(self.ventana, text="Generar Matricula", command=self.generar_matricula)
        self.boton_generar.pack()

        tk.Label(self.ventana, text="Matricula generada:").pack()
        self.entry_contraseña = tk.Entry(self.ventana)
        self.entry_contraseña.pack()


    def generar_matricula(self):
        longitud = self.longitud_var.get()
        especialesCar = self.CaracteresVar.get()

        generador = GeneradorMatricula()
        contraseña = generador.generar_matricula(longitud, especialesCar)

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
