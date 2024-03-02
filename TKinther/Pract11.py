from tkinter import Tk, Frame

#1.Cream la ventana 
Ventana= Tk() # Uso de POO creando un Objeto ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana
seccion1=Frame(Ventana,bd="grey")
seccion1.pack(expand=True,fill='both')
seccion2=Frame(Ventana,bd="deepblue")
seccion2.pack()
seccion3=Frame(Ventana,bd="black")
seccion3.pack()
#ejecuta (metodo que ejecuta la ventana creada)
Ventana.mainloop()