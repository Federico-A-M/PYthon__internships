# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:02:12 2022

@author: feder
"""


"""
Tuplas

6. Cartas como tuplas.
a. Proponer una representación con tuplas para las cartas de la baraja francesa.

52 cartas- cuatro palos(13 cartas)

b. Escribir un programa de poker que reciba cinco cartas 
de la baraja francesa e informe (devuelva el valor lógico correspondiente) 

si esas cartas forman o no un poker (es decir que hay 4 cartas con el mismo número).
"""                                                                
                                                                      
               
# import random
# cartas = ('Trebol', 'Diamante', 'Corazones', 'Picas')
# mazo = []
# for i in range(50):
#     if i < 12:
#         if i == 10 or i == 11 or i == 12:
#             if i == 10:
#                 mazo.append(('Jota', 'Trebol'))
#             if i == 11:
#                 mazo.append(('Reyna', 'Trebol'))
#             if i == 12:
#                 mazo.append(('Rey', 'Trebol'))
#         else:
#             if (i + 1) == 10:
#                 continue
#             if (i + 1) == 1:
#                 mazo.append(('AS', 'Trebol'))
#             else:
#                 mazo.append((i + 1, 'Trebol'))

#     if i >= 12 and i < 25:
#         if i - 12 == 10 or i - 12 == 11 or i - 12 == 12:
#             if i - 12 == 10:
#                 mazo.append(('Jota', 'Dimante'))
#             if i - 12 == 11:
#                 mazo.append(('Reyna', 'Dimante'))
#             if i - 12 == 12:
#                 mazo.append(('Rey', 'Dimante'))
#         else:
#             if (i - 12) == 10:
#                 continue
#             if i == 12:
#                 mazo.append(('AS', 'Dimante'))
#             else:
#                 mazo.append((i - 12, 'Dimante'))

#     if i >= 25 and i < 38:
#         if i - 25 == 10 or i - 25 == 11 or i - 25 == 12:
#             if i - 25 == 10:
#                 mazo.append(('Jota', 'Corazones'))
#             if i - 25 == 11:
#                 mazo.append(('Reyna', 'Corazones'))
#             if i - 25 == 12:
#                 mazo.append(('Rey', 'Corazones'))
#         else:
#             if (i - 25) == 10:
#                 continue
#             if i == 25:
#                 mazo.append(('AS', 'Corazones'))
#             else:
#                 mazo.append((i - 25, 'Corazones'))

#     if i >= 38 and i < 50:

#         if i - 37 == 10 or i - 37 == 11 or i - 37 == 12:
#             if i - 37 == 10:
#                 mazo.append(('Jota', 'Picas'))
#             if i - 37 == 11:
#                 mazo.append(('Reyna', 'Picas'))
#             if i - 37 == 12:
#                 mazo.append(('Rey', 'Picas'))
#         else:
#             if (i - 37) == 10:
#                 continue
#             if i == 38:
#                 mazo.append(('AS', 'Picas'))
#             else:
#                 mazo.append((i - 37, 'Picas'))


# carta1 = random.choice(mazo)
# carta2 = random.choice(mazo)
# carta3 = random.choice(mazo)
# carta4 = random.choice(mazo)
# carta5 = random.choice(mazo)

# iguales = 0
# mano = []
# mano_original = []
# for i in range(5):
#     carta = random.choice(mazo)
#     mano_original.append(carta)
#     if carta[0] in mano:
#         iguales += 1
#     else:
#         mano.append(carta[0])
# if iguales == 4:
#     print('POKER')
# else:
#     print('No Es PoKER:')
#     print('Cartas iguales: ', iguales)
#     print('Mano: ', mano_original)                                                       
                                                             
                                                                      
"""                                                      
7. El tiempo como tuplas.
a. Proponer una representación con tuplas para representar el tiempo.
b. Escribir un programa que reciba dos tiempos dados y devuelva su suma.
"""


# import random


# segundos=random.randint(0, 2**32)
# minutos=segundos//60
# horas=minutos//60
# dias=horas//24
# semanas=dias//7
# meses=semanas//4
# anios=meses//12

# tiempo_uno = ("años:", anios, 
#               "meses: ", meses, 
#               "semanas: ", semanas,
#               "dias: ", dias, 
#               "horas: ", horas,
#               "minutos :", minutos, 
#               "segundos : ", segundos)  


# segundos=random.randint(0, 2**32)
# minutos=segundos//60
# horas=minutos//60
# dias=horas//24
# semanas=dias//7
# meses=semanas//4
# anios=meses//12

# tiempo_dos = ("años:", anios, 
#               "meses: ", meses, 
#               "semanas: ", semanas,
#               "dias: ", dias, 
#               "horas: ", horas,
#               "minutos :", minutos, 
#               "segundos : ", segundos)  


# for i in tiempo_uno:
#         print(i)

# print("")

# for i in tiempo_dos:
#         print(i)


# tiempo_suma= ("años:", tiempo_uno[1]+tiempo_dos[1], 
#               "meses: ", tiempo_uno[3]+tiempo_dos[3], 
#               "semanas: ", tiempo_uno[5]+tiempo_dos[5],
#               "dias: ", tiempo_uno[7]+tiempo_dos[7], 
#               "horas: ", tiempo_uno[9]+tiempo_dos[9],
#               "minutos :", tiempo_uno[11]+tiempo_dos[11], 
#               "segundos : ", tiempo_uno[13]+tiempo_dos[13])  

# print(" ")
# print("La suma de los tiempos es igual a :")
# for i in tiempo_suma:
#         print(i)

"""
8. Escribir un programa que dada una fecha expresada como la terna (Día, Mes, Año)
 (donde Día, Mes y Año son números enteros) 
 calcule el día siguiente al dado, en el mismo formato.
"""

# import random


# dias=random.randint(1, 31)
# mes=random.randint(1, 12)
# anio=random.randint(0, 2022)


# fecha = ("DD: ", dias, "MM: ", mes, "AAAA:", anio)  

# for i in fecha:
#     print(i)
    
#     if i==dias : print("el siguiente dia sera: ", i+1)
    


"""
9. Escribir un programa que dada una fecha expresada como la terna (Día, Mes, Año)
(donde Día y Año son números enteros, y Mes es el texto "Ene", "Feb",. . ., "Dic", 
 según corresponda) calcule el día siguiente al dado, en el mismo formato.
"""

# import random


# dias=random.randint(1, 31)
# mes=random.randint(1, 12)
# anio=random.randint(0, 2022)


# if mes == 1:
#     mes = "Enero"
# if mes == 2:
#     mes = "Febrero"
# if mes == 3:
#     mes = "Marzo"
# if mes == 4:
#     mes = "Abril"
# if mes == 5:
#     mes = "Mayo"
# if mes == 6:
#     mes = "Junio"
# if mes == 7:
#     mes = "Julio"
# if mes == 8:
#     mes = "Agosto"
# if mes == 9:
#     mes = "Septiembre"
# if mes == 10:
#     mes = "Octubre"
# if mes == 11:
#     mes = "Noviembre"
# if mes == 12:
#     mes = "Diciembre"


# fecha = ("DD: ", dias, "MM: ", mes, "AAAA:", anio)  

# for i in fecha:
#     print(i)
    
#     if i==dias : print("el siguiente dia sera: ", i+1)



"""
10. Un analista económico utiliza un programa que toma desde una tupla valores
 de la cotización en pesos del dolar blue en los últimos 5 días:
"""

dolarBlue = ( "189 "," 1930 "," 187 "," 210 "," 202 ")

"""     
con el propósito de utilizarlos en un determinado informe. 

El programador se ha dado cuenta que necesita modificar la segunda posición 
del mismo, porque hay un error de entrada del dato.

 ¿Qué solución propone para enmendar este problema?.
""" 

 
 
 
 
 
""" 
11. Dada una lista de tuplas donde el elemento en la posición 0 es el DNI 
de la persona y en la posición 1 es el ingreso, 
identificar todas las personas cuyo ingreso es:
    
a. Menor que el salario mínimo, vital y móvil (SMVM)

b. Entre un SMVM y dos SMVM

c. Entre dos SMVM y 4 SMVM

d. Mayor a 4 SMVM

Crear una lista de tuplas donde el primer elemento indica el rango de ingresos y el segundo elemento
la cantidad de personas en ese segmento.
"""


# import random
# tuplas = []
# smvm = 45000  # hoy

# for i in range(20):
#     tuplas.append((random.randint(100000, 400000),
#                    random.randint(30000, 945000)))

# menorsmvm = 0
# dossmvm = 0
# cuatrosmvm = 0
# mascuatrosmvm = 0

# for i in tuplas:
#     if i[1] < 45000:
#         menorsmvm += 1
#     if i[1] >= 45000 and i[1] < 90000:
#         dossmvm += 1
#     if i[1] >= 90000 and i[1] < 180000:
#         cuatrosmvm += 1
#     if i[1] > 180000:
#         mascuatrosmvm += 1

# tuplassmvm = [('<45000', menorsmvm),
#               ('45000-90000', dossmvm),
#               ('90000-180000', cuatrosmvm),
#               ('>180000', mascuatrosmvm),
#               ]
# for i in tuplassmvm:
#     print('Rango: %s\nCantidad: %s' % (i[0], i[1]))