import dictionary as d
import math


     # Ejercicio 4

# O(2n) = O(n)

def isPermutation(elem1, elem2):
    
    if len(elem1) != len(elem2):
        return False
    
    sum1 = sum(ord(c) for c in elem1)       # Optimizacion de codigo, elimino lineas innecesarias  # O(n)
    sum2 = sum(ord(c) for c in elem2)       # O(n): 


    return sum1 == sum2


    # Ejercicio 5

# O(n + n^2) == O(n^2)
def isConj(elem):
    return len(elem) == len(ConvertToSet(elem)) # O(n):longitud lista + O(n^2):set, recorre todos los elem y saca los repetidos 

    # Ejercicio 6
def Codigo_postal_hash(cp):
    suma_ascii = 0
    k = 0
    for i in range(len(cp)):
        suma_ascii += ord(cp[i]) * 10**k 
        k += 1

    # primo_grande = 4332221111 quiero dar una funcion de hash, pero va a ocumar muchisimo espacio de esta forma
    return suma_ascii

    # Ejercicio 7
def compress(elem):

    if isConj(elem):
        return elem
    else:
        lista = ""
        cont = 0

        for i in range(len(elem)):
            if i == 0:
                lista += elem[i]
                cont += 1
                continue
            if elem[i] == lista[-1]:
                cont += 1
            else:
                lista += str(cont) + elem[i]
                cont = 1
        lista += str(cont)

        return lista
            
def ConvertToSet(elem):
    lista = []

    for i in range(len(elem)):
        if elem[i] not in lista:
            lista.append(elem[i])
        
    return lista


    # Ejercicio 8
    

#

def isIn(texto, cadena):        # Use un tipo de algoritmo llamado KMP (Knut - Morris - Pratt), investigar mas a fondo

    L_cadena = len(cadena)
    L_texto = len(texto)

    pref_table = [0]*(L_cadena)         # Creo una tabla del prefijo para poder facilitar el posicionamiento del señalador
    pointer = 0         # Señalador

    for i in range(1, L_cadena):        # Defino las repeticiones de las letras llenando la tabla

        while pointer > 0 and cadena[i] != cadena[pointer]:
            pointer = pref_table[pointer-1]
        if cadena[pointer] == cadena[i]:
            pointer += 1
            pref_table[i] = pointer

    pointer = 0 
    for i in range(L_texto):
        while pointer > 0 and cadena[pointer] != texto[i]:
            pointer = pref_table[pointer-1]
        if cadena[pointer] == texto[i]:
            pointer += 1
            if pointer == L_cadena:
                return i - L_cadena + 1




    return False




#def isSubConj(C, S):
