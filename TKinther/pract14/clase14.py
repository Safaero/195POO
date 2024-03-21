class Cuenta:
    def _init_(self, numero_cuenta, titular, edad, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
        
    def consultar_saldo(self):
        return self.saldo
    
    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad
        
    def retirar_efectivo(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("No hay suficiente saldo en la cuenta.")
        
    def depositar_a_otra_cuenta(self, otra_cuenta, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            otra_cuenta.ingresar_efectivo(cantidad)
        else:
            print("No hay suficiente saldo en la cuenta.")