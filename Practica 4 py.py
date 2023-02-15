# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:22:21 2022

@author: feder
"""


"""
Facultad de Ciencias Exactas, Ingeniería y Agrimensura (FCEIA - UNR)
Tecnicatura Universitaria en Inteligencia Artificial


                                    Programación 1

                                    Práctica 4:
    
1. Imprimir los primeros 20 números naturales.
"""

# for i in range(1,21):
#     print(i)


"""
2. Imprimir la tabla de multiplicar del número 5
"""

# for i in range(0, 11):
#     print(i*5)




"""
3. Imprima los números de -10 a -1.
"""

# for i in range(-10, -0):
#     print(i)



"""
4. Dada la siguiente secuencia de números:
numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50]
imprimir los números divisibles por 5 menores a 150.
"""


# ? preguntar, no entiendo por que da la secuencia



"""
5. Imprimir los primeros 10 valores de la secuencia de Fibonacci. La secuencia de Fibonacci 
es una serie de números en la cual los dos primeros números son 0 y 1, 
y el siguiente número se corresponde a la suma de los dos números anteriores. 

Resultado esperado:
0 1 1 2 3 5 8 13 21 34
"""


# a = 0
# b = 1
# c = 1

# for i in range(10):

#     if i<2:
#         print(i)
        
#     else:
#         print(c)
        
#         a = b
           
#         b = c
           
#         c = a+b


    
"""
6. Imprimir el valor factorial del número 5 usando un bucle. El valor factorial (símbolo: !) se obtiene de
multiplicar todos los números enteros desde el número elegido hasta 1. Resultado esperado: 120
"""

# n=5
# factorial=5

# for i in range(5):

    
#     if i==4:
#         print(factorial)
#         break

#     n-=1
#     factorial = (factorial*n)
    



"""
7. Explique el resultado de los siguientes programas
"""

# # a.
# lista = []
# for j in lista :
#     print ( j )

# no imprime nada por que no hay nada en el contenido, imprime dato null

# # b.

# i = 1
# for i in [1 , 2 , 3]:
#     print ( i )
#     print ( i )

# simplemente imprime dos veces i en las vueltas que itera, la primera declaracion global esta de mas


"""
8. Resuelva los siguientes ejercicios

"""

# a. Calcular el cuadrado de los primeros 10 números enteros.

# n=1
# for i in range(10):
    
#     print(n**2)
#     n+=1
    


# b. Calcular la suma de los números enteros entre 0 y 100 inclusive.

# R=0
# for i in range(101):
    
#     R += i
#     print(R)


# c. Calcular la suma de los números pares menores a 100. ¿Cuántos números pares hay menores a 100? (2550)

# R=0
# for i in range(0, 101, 2):
  
#         R += i
#         print(R)    
  


# d. Calcular la suma de los números impares menores a 100. ¿Cuántos números impares hay menores a 100?

R=0
for i in range(0, 100):

    if (i%2!=0):    
        R += i
        print(R)




"""
9. ¿Cuál es el problema asociado al siguiente programa? No hace falta ejecutarlo para responder esta
pregunta.
x = 0
while x < 5:
print ( x )

nunca sale del bucle por que siempre es cierto que mientras x valga cero sera menor que 5

"""






"""
10. Escriba un programa que dada una secuencia de números y un valor de umbral vaya sumando los
números de la secuencia hasta que la suma alcance el umbral. Utilice break para terminar la ejecución
del bucle cuando la suma alcance el umbral.

Resultados esperados:

umbral = 21
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
# suma -> 21
umbral = 34
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
# suma -> 34
umbral = 100
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
# suma -> 43
"""










"""
11. Escriba un programa que dada una secuencia numérica compute la suma de los números pares. Utilice
un bucle while y la sentencia continue para saltear los casos donde el número no sea par.
Resultados esperados:
valores = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8 , 9 , 10]
# suma -> 30
valores = [1 , 4 , 7 , 10]
# suma -> 14
"""








"""
12. Escriba un programa que solicite un numero entero al usuario y compute la suma de todos los numeros
naturales menores a él. Este programa debe ser interactivo. Es decir, el programa solicita un numero al
usuario, devuelve la suma, y solicita un nuevo número. Esto continúa así hasta que el usuario ingresa
"salir", determinando que el programa debe terminar. Utilice un bucle while para resolver este
problema. Tenga en cuenta la sentencia break para determinar la interrupción del bucle. Ejemplos:
Ingrese un numero o 'salir ' para terminar : 10
La suma es 45
Ingrese un numero o 'salir ' para terminar : 50
La suma es 1225
Ingrese un numero o 'salir ' para terminar : salir
"""









"""
13. Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. A partir de ahí, cada
día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que
la pila de billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar
a resolver el problema:
billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
altura_monumento = 70 # altura en metros
billetes_n = 1
dia = 1
Utilice un bucle while para resolver el problema.
"""








"""
14. Escriba un programa reciba dos números como parámetros, y compute cuántos múltiplos del primero
hay, que sean menores que el segundo.
a. Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b. Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor
que el segundo.
c. Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
2

"""