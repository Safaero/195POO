from Personaje import *
from Armas import *

spartan= Personaje ()

Arma= Armas ()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#usamos los metodos del spartan

spartan.correr(False)
spartan.lanzarGranada()

Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(65)