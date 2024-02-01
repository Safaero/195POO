peso_payaso = 112
peso_muñeca = 75

num_payasos = int(input('Introduce el número de payasos vendidos: '))
num_muñecas = int(input('Introduce el número de muñecas vendidas: '))

peso_total = num_payasos * peso_payaso + num_muñecas * peso_muñeca

print('El peso total del paquete será de', peso_total, 'gramos')