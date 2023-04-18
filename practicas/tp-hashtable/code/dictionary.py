class DictionaryNode:
    key = None
    value = None
    nextNode = None

   
        

def hash(A, k):
    #if         # Quiero poner condicion para utilizar distintas funciones de hash segun la situacion 
    return k % len(A)

    # Ejercicio 6
def Codigo_postal_hash(cp):
    suma_ascii = 0
    k = 0
    for i in range(len(cp)):
        suma_ascii += ord(cp[i]) * 10**k 
        k += 1

    # primo_grande = 4332221111 quiero dar una funcion de hash, pero va a ocumar muchisimo espacio de esta forma
    return suma_ascii


# def Ordered       # Estaria bueno implementar una manera de insertar los elementos en la tabla y que queden ordenados 
def insert(D, k, val):

    pos = hash(D,k)

    if D[pos] is None or D[pos] == 0:
        node = DictionaryNode()
        node.value = val
        node.key = k
        D[pos] = node
    else:
        node = DictionaryNode()
        node.value = val
        node.key = k
        node.nextNode = D[pos]
        D[pos] = node
        
    return D

def search(D, key):

    pos = hash(D, key)

    if D[pos] is None:
        return None
    else:
        node = D[pos]
        while node.nextNode is not None:
            if node.nextNode.key is not key:
                node = node.nextNode
            else:
                return node.key
        return None    

def delete(D, key):

    if search(D, key) is None:
        return None
    else:
        pos = hash(D, key)
        node = D[pos]

        if D[pos].key == key:
            D[pos] = node.nextNode
        else:
            while node.nextNode is not None:

                if node.nextNode.key != key:
                    node = node.nextNode
                else:
                    if node.nextNode.nextNode is None:
                        node.nextNode = None
                    else:
                        node.nextNode = node.nextNode.nextNode
            return D
        

    # Ejercicio 4

# O(2n) = O(n)

def isPermutation(elem1, elem2):
    
    if len(elem1) != len(elem2):
        return False
    
    sum1 = sum(ord(c) for c in elem1)       # Optimizacion de codigo, elimino lineas innecesarias  # O(n)
    sum2 = sum(ord(c) for c in elem2)       # O(n): 

    #sum1 = suma_Ascii(elem1)
    #sum2 = suma_Ascii(elem2)

    return sum1 == sum2


def suma_Ascii(elem):
    lista = list(elem)
    sum = 0
    for i in range(len(elem)):
        sum += ord(lista[i])  
    return sum

    # Ejercicio 5

# O(n + n^2) == O(n^2)
def isConj(elem):
    return len(elem) == len(ConvertToSet(elem)) # O(n):longitud lista + O(n^2):set, recorre todos los elem y saca los repetidos 

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


    # Ejercicio 9
    

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


    

