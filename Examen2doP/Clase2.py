import random

class GeneradorMatricula:
    def generar_matricula(self, nombre, apep, apem, nacimiento, curso, carrera):
        
        matricula = nombre[0] + apep[:2] + apem[:2] + nacimiento[-2:] + carrera[:3] + curso[-2:]

        matricula += ''.join(random.choices("0123456789", k=2))
        return matricula
