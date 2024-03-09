import random

class GeneradorContraseña:
    def __init__(self):
        self.caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def generar_contraseña(self, longitud, especialesCar):
        if especialesCar:
            self.caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?`~"

        contraseña = ''.join(random.sample(self.caracteres, longitud))
        return contraseña
