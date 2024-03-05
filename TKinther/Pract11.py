from tkinter import Tk, Frame, Button, messagebox
#metoos para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo','information'))
    
    print(messagebox.showerror('showerror','Error'))
    
    print(messagebox.showwarning('showwarning','WARNING!'))
    
    print(messagebox.askokcancel(message="¿Desea continuar?", title="soy el titulo"))

#
def addbtn():
    botonVerde.config(text="+")
    botonRosa= Button(seccion3,text="NUEVO", fg="#5E9193", bg="#D086E5")
    botonRosa.configure(width=5, height=3)
    botonRosa.pack()
    
#1.Cream la ventana 
Ventana= Tk() # Uso de POO creando un Objeto ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana
seccion1=Frame(Ventana,bg="grey")
seccion1.pack(expand=True,fill='both')
seccion2=Frame(Ventana,bg="#5A8E41")
seccion2.pack(expand=True,fill='both')
seccion3=Frame(Ventana,bg="black")
seccion3.pack(expand=True,fill='both')

#posicionar botones
#place
botonAzul= Button(seccion1,text="AZUL", fg="#5E9193", bg="#9CE3FD")
botonAzul.place(x=250,y=60, width=100, height=30)
#grid
botonNegro= Button(seccion2,text="NEGRO", fg="#535F2C", bg="#000000")
botonNegro.configure(width=10, height=2)
botonNegro.grid(row=5,column=6)

botonAmarillo= Button(seccion2,text="YELLOW", fg="#000000", bg="#F7DC1E",command=mostrarMensajes)
botonAmarillo.configure(width=10, height=2)
botonAmarillo.grid(row=5,column=5)

botonVerde= Button(seccion3,text="VERDE", fg="#000000", bg="#32AE94",command=addbtn)
botonVerde.configure(width=10, height=2)
botonVerde.pack()
#ejecuta (metodo que ejecuta la ventana creada)

Ventana.mainloop()