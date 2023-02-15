


"""
                                    Diccionarios
                                    
                                    
12. Escribe un programa que lea una cadena y devuelva un diccionario 
con la cantidad de apariciones de cada palabra en la cadena. 

Por ejemplo:
"la peluca de la abuela "

# Debería mostrar
{"la": 2 , " peluca ": 1 , "de": 1 , " abuela ": 1}
"""

# frase="la peluca de la abuela"

# lista_dividida= frase.split

# diccionario={}

# aux=""
# cont=0


# for i in range(len(lista_dividida())):
    

#     aux = lista_dividida()[i]       

    
#     for j in lista_dividida():
#         if j==aux:
#             cont+=1
            
#     diccionario[aux]= cont
        
#     cont=0

    

# print(diccionario)




"""
13. Escribir un programa que toma una lista de tuplas con el formato 
(Alumno, Nota) 
donde alumno es una cadena con el nombre del alumno y nota es un número. 

lista = [(’Perez’, 8), (’Gonzalez’, 10), (’Fernandez’, 10)]


a. Crear un diccionario donde las claves son los alumnos 
y el valor asociado una lista que contenga las notas del alumno.


Ejemplo_dict = { 'Perez ': 8 , 'Gonzalez ': 10 , 'Fernandez ': 10}



b. Crear un diccionario donde las claves son las notas y 
el valor asociado una lista que contenga los
alumnos que obtuvieron esa nota en un parcial
Ejemplo_dict2 = {8: [ 'Perez '] , 10: ['Gonzalez ', 'Fernandez ']}
"""

# El defaultdict proporciona un contenedor de diccionario de valores predeterminado
#  para asignar la lista de valores correspondiente a las claves,
#  de modo que no necesitemos inicializar las claves con una lista vacía 
#  y el bucle se usa para extraer valores similares de la tupla.

# from collections import defaultdict #muy util para convertir listas con tuplas en dicc
  
# lista = [("Marco Aurelio",7),("Jose Antoni",2),("Francisco Sossa",2),("Brunilda Porota",9)]
  
# print("La lista original era : " + str(lista)) 
# print(" ")  

# diccionario = defaultdict(list) 
# diccionario_invertido = defaultdict(list)

# for i, j in lista: 
    # diccionario[i].append(j) 
  
# print("La fusion con el diccionario es : " + str(dict(diccionario))) 

# print(" ")
# for i, j in lista: 
#     diccionario_invertido[j].append(i) 
  
# print("La fusion con el diccionario es : " + str(dict(diccionario_invertido))) 



"""
14. Escribir un programa que recibe un diccionario que tiene como llave a alumnos 
y los valores asociados una lista con las notas de parciales de los alumnos. 
El programa debe calcular el promedio de cada alumno e imprimirlo en pantalla. 

Por ejemplo para
alumnos = {" Juan ": [6 ,9 ,8] , " Manuel ": [9 ,10 ,9] , " Martin ": [5 ,6 ,7]}

Debería mostrar
3


El promedio de Juan es 7.666666
El promedio de Manuel es 9.333333
El promedio de Martin es 6
"""



# alumnos = {"Juan": [6 ,9 ,8] , "Manuel": [9 ,10 ,9] , "Martin": [5 ,6 ,7]}
# prom=0

# for values, keys in alumnos.items():
    
#     for i in keys:
#         prom+=i
        
#     print("El promedio de",values,"es",(prom/3)) ; prom=0
    


"""
15. Repita el ejercicio 3 pero utilizando un diccionario. 
Ahora un número puede repetirse varias veces.
"""

#no me salio el 3


"""
16. Dadas dos listas donde la primera contiene nombres de personas y la segunda 
sus edades, generar un diccionario a partir de ellas. 
Investigar cómo la función zip() puede ayudar en la resolución
"""











"""
17. Dado un diccionario donde la clave es el DNI (formato cadena) 
y el valor es la cantidad de dosis de vacunas contra el covid, 
filtrar del mismo las personas que tienen 2 dosis y guardarlas en la estructura
de datos que crea conveniente. Esta información será uilizada para recordarles 
que ya tienen disponible la tercera dosis.
"""












"""
18. Un investigador de historia de la informática encontró un documento 
sin membrete, que data de mitad de siglo XX, 
e incluye un mensaje en código morse que sospecha explicaría importantes sucesos
históricos de la posteridad. 

Por lo tanto, para avanzar en su investigación es necesario descifrarlo, pero
no sabe el código. 



Dado el siguiente diccionario que permite descifrar un mensaje morse, ayude al
investigador en su tarea mediante un programa que le permita decodificar el mensaje.

morse = {
'A': '. -', 'B': ' -... ', 'C': ' -. -. ',
'D': ' -.. ', 'E': '.', 'F': '.. -. ',
'G': ' - -.', 'H': '.... ', 'I': '.. ',
'J': '. - - -', 'K': ' -. -', 'L': '. -.. ',
'M': '--', 'N': ' -.', 'O': '---',
'P': '. - -. ', 'Q': ' - -. -', 'R': '. -. ',
'S': '... ', 'T': '-', 'U': '.. - ',
'V': '... - ', 'W': '. - -', 'X': ' -.. - ',
'Y': ' -. - -', 'Z': ' - -.. ', '1': '. - - - -',
'2': '.. - - - ', '3': '... - - ', '4': '.... - ',
'5': '..... ', '6': ' -.... ', '7': ' - -... ',
'8': ' - - -.. ', '9': ' - - - -.', '0': ' -----',
'.': '. -. -. - ', ',': ' - -.. - - ', ':': ' - - -... ',
';': ' -. -. -. ', '?': '.. - -.. ', '!': ' -. -. - - ',
'"': '. -.. -. ', "'": '. - - - -. ', '+': '. -. -. ',
'-': ' -.... - ', '/': ' -.. -. ', '=': ' -... - ',
'_': '.. - -. - ', '$': '... -.. - ', '@': '. - -. -. ',
'&': '. -... ', '(': ' -. - -. ', ')': ' -. - -. - '
}



Código:
['.', ' -.', '.. - -. - ', '.', '. -.. ', '.. - -. - ', '.. -. ', '.. - ', '-', '.. - ',
'. -. ', '---', '.. - -. - ', '.', '... ', '.. - -. - ', '. - -. ', '---', '... ',
'.. ', ' -... ', '. -.. ', '.', '.. - -. - ', ' - -. -', '.. - ', '.', '.. - -. - ',
'. -.. ', '---', '... ', '.. - -. - ', '---', '. -. ', ' -.. ', '.', ' -.',
'. -', ' -.. ', '---', '. -. ', '.', '... ', '.. - -. - ', ' -.', '---',
'.. - -. - ', '. - -. ', '.', '... ', '.', ' -.', '.. - -. - ', '--', '. -',
'... ', '.. - -. - ', ' -.. ', '.', '.. - -. - ', '. - - - -', ' - -.. - - ', '..... ',
'.. - -. - ', '-', '---', ' -.', '.', '. -.. ', '. -', ' -.. ', '. -', '... ',
'. -. -. - ', '.. - -. - ', ' -.... - ', ' -.... - ', '.. - -. - ', '. - -. ', '---',
'. - -. ', '.. - ', '. -.. ', '. -', '. -. ', '.. - -. - ', '--', '.', ' -. -. ',
'.... ', '. - -. ', '.. ', ' -. -. ', '... ', ' - -.. - - ', '.. - -. - ', '. - - - -',
' - - - -.', '.... - ', ' - - - -.', ' - - -... ']
"""











"""
19. Cada profe de programación 1 tiene un diccionario donde guarda 
el legajo de cada alumne en la clave y una lista con las notas de cada persona
en el valor. 

Al cerrar el cuatrimestre, necesitan pasarle a alumnado un solo diccionario 
con estos datos, generarlo. 


Revisar el método .update() para ver como
puede ayudarte a resolver el problema. 



Los diccionarios de cada comisión se ven así

com1 = {'legajo_11 ': [6 , 7 , 8] ,... , 'legajo_1m ': [3 , 8 , 9]}
com2 = {'legajo_21 ': [6 , 7 , 8] ,... , 'legajo_2n ': [3 , 8 , 9]}
com3 = {'legajo_31 ': [6 , 7 , 8] ,... , 'legajo_3j ': [3 , 8 , 9]}
com4 = {'legajo_41 ': [6 , 7 , 8] ,... , 'legajo_4k ': [3 , 8 , 9]}

El diccionario final debería verse así:
    
prog_1 = {'legajo_11 ': [6 , 7 , 8] ,... , 'legajo_1m ': [3 , 8 , 9] ,
'legajo_21 ': [6 , 7 , 8] ,.. , 'legajo_2n ': [3 , 8 , 9] ,
'legajo_31 ': [6 , 7 , 8]... , 'legajo_3j ': [3 , 8 , 9] ,
'legajo_41 ': [6 , 7 , 8] ,... , 'legajo_4k ': [3 , 8 , 9]}
"""