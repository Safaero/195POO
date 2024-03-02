from Personaje import *
from Armas import *

#solicitar datos Spartan
print("datos del spartan")
nombreS= input("Escriba nombre del spartan")
especieS= input("Escribir su especie")
alturaS= float(input("escribir altura de spartan"))
print(" ")
print("datos del villano")
nombreN= input("Escriba nombre del nemesis")
especieN= input("Escribir su especie")
alturaN= float(input("escribir altura de nemesis"))
print(" ")

spartan= Personaje (especieS,nombreS,alturaS)
Nemesis= Personaje (especieN,nombreN,alturaN)
Arma= Armas ()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#usamos los metodos del spartan

spartan.correr(False)
spartan.lanzarGranada()

Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(65)