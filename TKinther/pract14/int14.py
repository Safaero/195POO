import tkinter as tk

class CajaPopularApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Caja Popular")
        
        self.label_numero_cuenta = tk.Label(master, text="Número de Cuenta:")
        self.label_numero_cuenta.grid(row=0, column=0)
        self.entry_numero_cuenta = tk.Entry(master)
        self.entry_numero_cuenta.grid(row=0, column=1)
        
        self.label_titular = tk.Label(master, text="Titular:")
        self.label_titular.grid(row=1, column=0)
        self.entry_titular = tk.Entry(master)
        self.entry_titular.grid(row=1, column=1)
        
        self.label_edad = tk.Label(master, text="Edad:")
        self.label_edad.grid(row=2, column=0)
        self.entry_edad = tk.Entry(master)
        self.entry_edad.grid(row=2, column=1)
        
        self.label_saldo = tk.Label(master, text="Saldo:")
        self.label_saldo.grid(row=3, column=0)
        self.entry_saldo = tk.Entry(master)
        self.entry_saldo.grid(row=3, column=1)
        
        self.consultar_saldo_button = tk.Button(master, text="Consultar Saldo", command=self.consultar_saldo)
        self.consultar_saldo_button.grid(row=4, column=0)
        
        self.ingresar_efectivo_button = tk.Button(master, text="Ingresar Efectivo", command=self.ingresar_efectivo)
        self.ingresar_efectivo_button.grid(row=4, column=1)
        
        self.retirar_efectivo_button = tk.Button(master, text="Retirar Efectivo", command=self.retirar_efectivo)
        self.retirar_efectivo_button.grid(row=5, column=0)
        
        self.depositar_cuenta_button = tk.Button(master, text="Depositar a Otra Cuenta", command=self.depositar_cuenta)
        self.depositar_cuenta_button.grid(row=5, column=1)
        
    def consultar_saldo(self):
        
        pass
        
    def ingresar_efectivo(self):

        pass
        
    def retirar_efectivo(self):

        pass
        
    def depositar_cuenta(self):
        pass

root = tk.Tk()
app = CajaPopularApp(root)
root.mainloop()