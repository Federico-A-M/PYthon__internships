

"""
 -------------- iterar listas (recorrerla)-------------------
 
Podemos iterar una lista con un for:
"""
# numeros = [ 7, 9, 24, 8 ]

# for index, value in enumerate(numeros):
#     print(index, value)

"""
Tambien podemos usar indices:
"""

# numeros = [ 7, 9, 24, 8 ]

# for i in range(len(numeros)):
#     print( numeros[i])


"""
Práctica 5:
                                                                                    
Listas
                                        
1. Escriba los siguientes programas. Nota: No utilice los metodos index, min, max, reverse.

a. Dada una lista de números list y un número n, determine en qué índice de la lista list se
encuentra el número n. En caso de no encontrarlo, el programa mostrará -1. 
"""


# # Ejemplos
# list = [11 ,25 ,3 , -4 ,95]
# n = 3
# # El programa debería mostrar (2)

# aux=0

# for i in list:

#     if i==n:
#         print(aux)

#     aux+=1


# list = [1 ,2 ,3 ,4 ,5]
# n = 10
# # El programa debería mostrar (-1)

# aux=-1

# for j in list:
#     aux+=1
#     print(aux)

# for i in list:

#     aux-=1

#     if i==n:
#         print(aux)

# print(aux)


"""
b. Dada una lista de números, calcule el mínimo y el máximo de la lista. 
Nota: es posible hacerlo recorriendo una única vez la lista o recorriéndola dos veces. 
Piense las ventajas y desventajas de ambos métodos.
"""

# numeros = [11, 25, 3, -4, 95]
# El programa deber ía mostrar

# El mínimo es -4
# El máximo es 95

# f = max(numeros)
# print(f)

# f = min(numeros)
# print(f)

# maxi=0
# mini=maxi

# for i in numeros:

#     if i>maxi:
#         maxi=i


#     if i<mini:
#         mini=i

# print(maxi)

# print(mini)


"""
c. Dada una lista de números, cree una nueva lista sumando 1 a cada elemento.
"""

# numeros = [0 ,1 ,2 ,3 ,4]
# # El programa deber ía mostrar
# # [1 ,2 ,3 ,4 ,5]
# numeros_mas_uno=[]

# for i in numeros:
#     numeros_mas_uno.append(i+1)

# print(numeros_mas_uno)


"""
d. Dada una lista palabras de cadenas de texto, devuelva una nueva lista formada sólo por las
cadenas de palabras que empiezan con "a".
"""

# palabras = ["arbol", "barco", "artificial", "casa", "dado", "a"]
# # El programa deber ía mostrar
# # ["arbol", "artificial", "a"]

# pasa_palabras=[]
# j=0

# for i in palabras:

#     if i[0]=="a":
#         pasa_palabras.append(palabras[j])

#     j +=1

# print(pasa_palabras)


"""
e. Dada una lista de números, calcule, por un lado, la suma de los elementos que se encuentran 
en un índice par en la lista 

y, por otro lado, el producto de los elementos de posiciones con índice impar.
"""

# numeros = [0,1,2,3,4,5]
# El programa deber ía mostrar
# La suma de índices pares es 6
# El producto de índices impares es 15

# pares=0
# impares=1

# for i in numeros:

#     if i%2==0:
#         pares+=i
#     else:
#         impares*=i

# print( "pares: ", pares, " / impares:", impares)


"""
f. Dada una lista cualquiera, cree una nueva lista con los mismos elementos 
pero en el orden inverso.
"""
# numeros = [0 ,1 ,2 ,3 ,4 ,5]
# # # El programa debería mostrar
# # # [5 ,4 ,3 ,2 ,1 ,0]


# print("")
# print(sorted(numeros, reverse=True)) #genial...


"""
2. Escriba un programa que dada una lista de números list devuelva otra lista 
cuyos elementos sean las sumas acumuladas de los elementos de list en cada posición.

Es decir, 
una nueva lista donde 

el primer elemento es el mismo que en la lista original list,

el segundo elemento es la suma del primer y segundo elementos de list, 
el tercer elemento es la suma del resultado anterior con el tercer elemento
de la lista original y así sucesivamente. 

Por ejemplo, dada la lista [1, 2, 3], la suma acumulada debería ser [1, 3, 6].
"""


# lista=[1,2,3]
# sum=0
# atsil=[]

# for i in range(len(lista)):
#     print("iterador: ",i)

#     if i==0:
#         atsil.append(lista[i])
#     else:
#         print("elemento suma: ",sum)
#         atsil.append(lista[i]+sum)
#         sum+=lista[i]
#         continue


#     sum+=lista[i]

# print(atsil)


"""
3. Escriba un programa que dada una lista 
determine si tiene algún elemento repetido e imprimirlos. 
Puede asumir que un numero se repite a lo sumo una vez. 

Pista: Utilice slicing de listas.

    Ejemplo de fotocopia::
    
        alumno = [7, “Jose”, 24, 2022]

        print( alumno[-2:] ) #slicing retorna una nueva lista --> [24, 2022]
        print( alumno[1:3] -->  [“Jose”, 24].
"""


# no saleeee !!!!!!!!!!!!!!!!!!!!



# datos = [1, 1, 1]
# # print(datos[1:2])
# # del datos[1]
# # print(datos)

# datos_set = datos


# for i in range(len(datos)):

    
#     if (datos_set[i])==(datos_set[i:i+1]):
#         del datos_set[i]
        

# print(datos)
# print(datos_set)

        


# lista = [1,2,3,4,5, 5]

# if len(lista) == len(set(lista)): #metodo set de python sacado de internet
#     print("no hay elementos repetidos")
# else:
#     print("hay elementos repetidos")



"""
4. Calcule los n primeros números de la secuencia de Fibonacci en una lista. 
Es decir, el programa comenzara con la lista [0,1] y computará iterativamente 
el siguiente número de la secuencia.
"""

# fibo=[0,1]

# #fibo.append(fibo[0] + fibo[1]) #indice 2
# #fibo.append(fibo[1] + fibo[2]) #indice 3

# for i in range(8): #0 - 7
#     #fibo.append(fibo[-2] + fibo[-1])
#     #fibo.append( fibo [len(fibo) -2 ] + fibo[len(fibo) -1])
#     fibo.append(fibo[i] + fibo[i+1])
    
# print(fibo)
    
    
    
"""
5. El objetivo de este ejercicio es recolectar datos de personas y almacenarlos 
en una especie de base de datos. 
A través de lo diferentes ítems, los iremos guiando en la creación de la misma.


a. Escribir un programa que le pida al usuario ingresar por consola los siguientes datos
por separado: Nombre, Apellido, Localidad, Edad, DNI, Carrera universitaria en curso, 
año de inicio de la carrera. 

Guardar los datos en una lista llamada datos_personales e imprimirlos en pantalla.

ejemplo : ['María', 'Gonzalez ', 'Chascomús', 24 , 50708934 ,'Ing . civil ', 2019]
"""

# datos_personales=[]


# nombre= "fede" #input("Ingrese su nombre: ")
# datos_personales.append(nombre)
# print("")
# apellido= "aquino"      #input("Ingrese su apellido: ")
# datos_personales.append(apellido)
# print("")
# localidad= "Rosario"         #input("Ingrese su localidad: ")
# datos_personales.append(localidad)
# print("")
# edad= 31          #int(input("Ingrese su edad: "))
# datos_personales.append(edad)
# print("")
# dni=  35583945              #int(input("Ingrese su dni: "))
# datos_personales.append(dni)
# print("")
# carrera= "Artes"       #input("Carrera en curso: ")
# datos_personales.append(carrera)
# print("")
# anio_de_inicio= 2013        #int(input("Ingrese el año de inicio: "))
# datos_personales.append(anio_de_inicio)
# print("")


# print(datos_personales)


"""
b. A partir de la lista del ejercicio anterior, 
genere un programa que calcule los años que la persona lleva cursando la carrera
y lo agregue a la lista. Por ejemplo, si la persona inició su carrera en el
2019, la cantidad de años cursados a agregar es 4.

ejemplo : ['María', 'Gonzalez', 'Chascomús', 24 , 50708934 , 'Ing . civil ', 2019 , 4]

Finalmente, imprima una frase que indique el nombre, el apellido y 
cantidad de años cursados de la persona
"""

# anios_cursados=2022

# for i in datos_personales:
#     if i == anio_de_inicio:
#         anios_cursados-=anio_de_inicio
#         datos_personales.append(anios_cursados)

# print("EL alumno ", datos_personales[0], "", datos_personales[1], "lleva cursando ", datos_personales[7], "años")


"""
c. Utilice el código de los ítems de arriba y automatice la recolección 
de datos para una cantidad de personas desconocidas. 

El resultado de este ejercicio debe ser una lista llamada basedatos donde
se almacenarán las listas datos_personales de cada individuo que se recolecten
"""

base_de_datos=[]
datos_personales=[]
centinel=""

    
centinel = input("Bienvenido a al sistema de datos de la escuela\
                 Benito Juarez, acontinuan ingrese los datos del alumnado: enter para continuar ")

print("")

while centinel!="*":
    
    datos_personales=[]

    nombre=input("Ingrese su nombre: ")
    datos_personales.append(nombre)
    print("")
    apellido=input("Ingrese su apellido: ")
    datos_personales.append(apellido)
    print("")
    localidad=input("Ingrese su localidad: ")
    datos_personales.append(localidad)
    print("")
    edad=int(input("Ingrese su edad: "))
    datos_personales.append(edad)
    print("")
    dni=int(input("Ingrese su dni: "))
    datos_personales.append(dni)
    print("")
    carrera=input("Carrera en curso: ")
    datos_personales.append(carrera)
    print("")
    anio_de_inicio=int(input("Ingrese el año de inicio: "))
    datos_personales.append(anio_de_inicio)
    print("")

    anios_cursados=2022

    for i in datos_personales:
        if i == anio_de_inicio:
            anios_cursados-=anio_de_inicio
            datos_personales.append(anios_cursados)


    print(" ")
    
    base_de_datos.append(datos_personales)
    
    
    centinel = input("Si Desea agregar un nuevo ingreso a la base de datos?\
                     prescione cualquier tecla para continuar,\
                      de lo contrario precione ( * ) para salir: ")
    


print(base_de_datos)

"""
d. Realice un programa que modifique para cada persona la carrera en curso 
por la palabra "TUIA".
"""

for i in range(len(base_de_datos)):
    
    for j in base_de_datos[i]:
        
        if j == carrera:
            carrera="TUIA"
            print(j)