import random

class GeneradorMatricula:
    def __init__(self):
        self.caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def generar_matricula(self, longitud, especialesCar):
        if especialesCar:
            self.caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?`~"

        contraseña = ''.join(random.sample(self.caracteres, longitud))
        return contraseña
