import tkinter as tk
from tkinter import messagebox
from Clase2 import GeneradorMatricula
class InterfazGenerador:
    
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Examen 2 :)")

        self.nombre_var = tk.StringVar(value='')
        self.apep_var = tk.StringVar(value='')
        self.apem_var = tk.StringVar(value='')
        self.nac_var = tk.StringVar(value='')
        self.curs_var = tk.StringVar(value='')
        self.carrer_var = tk.StringVar(value='')

        tk.Label(self.ventana, text="Nombre:").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.nombre_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="Apellido paterno").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.apep_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="Apellido materno").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.apem_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="Año de nacimiento").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.nac_var)
        self.entry_longitud.pack()
        
        tk.Label(self.ventana, text="carrera:").pack()
        self.entry_longitud = tk.Entry(self.ventana, textvariable=self.carrer_var)
        self.entry_longitud.pack()


        self.boton_generar = tk.Button(self.ventana, text="Generar Matricula", command=self.generar_matricula)
        self.boton_generar.pack()

        tk.Label(self.ventana, text="Matricula generada:").pack()
        self.entry_contraseña = tk.Entry(self.ventana)
        self.entry_contraseña.pack()


    def generar_matricula(self):
        Nombre = self.nombre_var.get()
        Apep = self.apep_var.get()
        Apem = self.apem_var.get()
        Nacimiento = self.nac_var.get()
        Curso = self.curs_var.get()
        Carrera = self.carrer_var.get()
        Random = self.rando_var.get()

        generador = GeneradorMatricula()
        contraseña = generador.generar_matricula(Nombre, Apep, Apem, Nacimiento, Curso, Carrera, Random)

        self.entry_contraseña.delete(0, tk.END)
        self.entry_contraseña.insert(0, contraseña)
        
ventana = tk.Tk()
app = InterfazGenerador(ventana)
ventana.mainloop()
