# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:31:20 2022

@author: feder
"""
"""
                                    Practica 3:
    
1. Dada una contraseña verificar que su longitud es superior a 8 caracteres.
"""
#Contrasenia = input("Por favor ingrese a continuacion su contraseña de 8 digitos: ")

#if len(Contrasenia)>8:
#    print("acceso concedido")
#else:
#    print("Su contraseña es incorrecta")


"""
2. Escribir un programa que verifique si un numero es divisible por 4
"""

#num = int (input("ingrese un numero"))

# resto = num%4

# if resto==0:
    # print(" el numero es divisible por 4")
# else:
#         print(" el numero no es divisible por ")


"""
3. Determinar e informar el mayor valor de 3 numeros enteros. 
¿Que cambiarıas en el algoritmo si se trataran de 3 numeros reales 
o de 3 caracteres o de 3 palabras?. 
¿Y si se buscara el menor valor?
"""

# num1 = 1
# num2 = 5
# num3 = 10

# mayor = 0

# if num1 > num2:
#     mayor=num1
# else:
#     mayor=num2
    
# if mayor<num3:
#     mayor=num3

# print("El mayor numero entre:" , num1, " ", num2, " y ", num3, " es ", mayor)



"""
4. Dados 3 lados de un triangulo, 
informar si el mismo es equilatero, isosceles o escaleno.
"""

# cat1=8
# cat2=8
# cat3=8

# if cat1==cat2==cat3:
#     print("El Triangulo es equilatero")
# elif cat1!=cat2!=cat3:
#     print("El triangulo es escaleno")
# else:
#     print("El triangulo es isoceles")


"""
5. Convertir las calificaciones alfabeticas ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’ 
en calificaciones numericas 5, 6, 7, 8, 9 y 10 respectivamente. 
Ingresar una calificacion alfabetica e informar por pantalla la calificacion
numerica correspondiente, en caso de ingresar cualquier otra letra mostrar 
((error calificacion inexistente)).
"""

# print("Ingrese la calificacion correspondiente al alumno: ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’")
# print("")
# print("")
# calificacion = input("...")

                     
# if  calificacion=='I' or calificacion=='i':
#     print("la calificacion fue registrada como 5")
# elif calificacion=='A' or calificacion=='a':
#     print("la calificacion fue registrada como 6")
# elif calificacion=='B' or calificacion=='b':
#     print("la calificacion fue registrada como 7")
# elif calificacion=='M' or calificacion=='m':
#     print("la calificacion fue registrada como 8")
# elif calificacion=='D' or calificacion=='d':
#     print("la calificacion fue registrada como 9")
# elif calificacion=='E' or calificacion=='e':
#     print("la calificacion fue registrada como 10")
# else:
#     print(" El valor ingresado no es correcto...")



"""
6. Escribir un programa que le pregunte a las personas su fecha de cumpleanos y 
en base a eso imprimir su signo zodıaco. 
Recomendacion, pedirle a la persona ingresar la fecha con cierto formato, por ejemplo
DD/MM y si la persona no lo respeta, imprimir un mensaje de error.
"""

# print("")
# print("Ingrese su fecha de cumpleaños a cotinuacion: ")
# print("")

# DD = int(input("Ingrese su dia de nacimiento: "))
# print("")

# MM = int(input("Ingrese el numero correspondiente al mes en que nacio: "))
# print("")              
       
# if (((DD>=20 and DD<31)and MM==1)or((DD>0 and DD<=18) and MM==2)):
#     print("Acuario")
# elif (((DD>=19 and DD<28) and MM==2)or((DD>0 and DD<=20) and MM==3)):
#     print("Piscis")
# elif (((DD>=21 and DD<30) and MM==3)or((DD>0 and DD<=19) and MM==4)):
#     print("Aries")
# elif (((DD>=20 and DD<31) and MM==4)or((DD>0 and DD<=21) and MM==5)):
#     print("Tauro")
# elif (((DD>=21 and DD<30) and MM==5)or((DD>0 and DD<=20) and MM==6)):
#     print("Geminis")
# elif (((DD>=21 and DD<31) and MM==6)or((DD>0 and DD<=22) and MM==7)):
#     print("Cancer")
# elif (((DD>=23 and DD<30) and MM==7)or((DD>0 and DD<=22) and MM==8)):
#     print("Leo")
# elif (((DD>=23 and DD<31) and MM==8)or((DD>0 and DD<=22) and MM==9)):
#     print("Virgo")
# elif (((DD>=23 and DD<30) and MM==9)or((DD>0 and DD<=22) and MM==10)):
#     print("Libra")
# elif (((DD>=23 and DD<31) and MM==10)or((DD>0 and DD<=21) and MM==11)):
#     print("Escorpio")
# elif (((DD>=22 and DD<30) and MM==11)or((DD>0 and DD<=21) and MM==12)):
#     print("Sagitario")
# elif (((DD>=22 and DD<31) and MM==12)or((DD>0 and DD<=19) and MM==1)):
#     print("Capricornio")
# else:
#     print(" los valores ingresado son incorrectos...")





"""
7. En el centro de la ciudad de Rosario el estacionamiento en vıa se encuentra tarifado
 y esta dividido en tres zonas con tarifas diferenciadas. 
 
El vehıculo puede estacionarse como maximo por 3 horas en el mismo sitio, 
 
luego de este tiempo, para renovar el servicio, hay que mover el vehıculo. 

La siguinte tabla muestra los costos por hora en cada una de las zonas:
    
Zona    Primer hora    Segunda hora    Tercer Hora
A         $57,00          $71,20         $85,50
B         $47,00          $58,70         $70,50
C         $37,00          $46,20         $55,50


Escribir un programa que dada la zona, A, B o C, y la cantidad de horas que el vehıculo estara
estacionado, devuelva el costo a pagar. En caso de que el tiempo de estacionamiento 
supere las 3 horas,imprimir un mensaje de error acorde.
"""


# print("")
    
# from random import*

# #Sintaxis: randint(int1,int2)
# zona = randint(1,3)
# if zona==1:
#     zona="A"
# elif zona==2:
#     zona="B"
# else:
#     zona="C"

# print("La zona en la que esta por aparcar es del tipo: ",zona)
# print("")

# time = int(input("Ingrese la cantidad de horas que estacionara el carro"))
# print("")

# if zona=="A" :
#     if time==1:
#         print("Total a pagar: $57,00 ")
#     elif time==2:
#         print("Total a pagar: $71,20")
#     elif time==3 :
#         print("Total a pagar: $85,50")
#     else:
#         print("Error: No puede aparcar mas de tres horas")
# elif zona=="B":
#     if time==1:
#         print("Total a pagar: $47,00")
#     elif time==2:
#         print("Total a pagar: $58,70")
#     elif time==3 :
#         print("Total a pagar: $70,50")
#     else:
#         print("Error: No puede aparcar mas de tres horas")
# elif zona=="C":
#     if time==1:
#         print("Total a pagar: $37,00")
#     elif time==2:
#         print("Total a pagar: $46,20")
#     elif time==3 :
#         print("Total a pagar: $55,50")
#     else:
#         print("Error: No puede aparcar mas de tres horas")
# else:
#     print("SysError: #fof4.165")




"""
8. Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local:

Item        Rosario         Funes       Roldan
Zapatillas     30 %          40 %         25 %
Remeras        20 %          30 %         15 %
Pantalones     10 %           5 %         20 %

Dado un item y la sede del local, devolver el descuento que se recibira.
"""








"""
9. Ahora, supongamos que ademas dependiendo del dıa de la semana 
se puede recibir un descuento adicional acumulable.

Es decir, si se recibio un descuento del 10 % segun el ıtem y la sede
y la compra se realiza un lunes, el descuento total ser´a un 20 % . 

Escribir un programa en el que la persona pueda ingresar el dıa de la semana,
el item a comprar y la sede del local. 

Luego, informar el descuento total a recibir. 

Utilizar la siguiente tabla de descuentos

            Lunes      Miercoles    Jueves
Descuento     10 %        8 %         5 %
"""