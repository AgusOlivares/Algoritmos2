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

def isPermutation_ver2(elem1, elem2):   

    """
    El orden de complejidad es de O(n), las operaciones de busqueda e insercion son O(1) pero depende de la longitud del elemento
    insertado por lo que sera O(n)
    """

    flag = True

    if len(elem1) != len(elem2):
        flag = False

    m = 27 # caracteres desde la a - z 
    hash_function = lambda k : ord(k) % m

    dicc = d.Dictionary(hash_function, m)
    for i in elem1:
        dicc.insert(dicc.D, i, str(i))
    for i in elem2:
        pos = dicc.search(dicc.D, i)

        if pos == None:
            flag = False
    
    return flag





    # Ejercicio 5

# O(n + n^2) == O(n^2)
def isConj(elem):
    return len(elem) == len(ConvertToSet(elem)) # O(n):longitud lista + O(n^2):set, recorre todos los elem y saca los repetidos 


def isConj_v2(elem): 

    """
    Complejidad de O(n) ya que el las operaciones de insercion busqueda y delete son O(1)
    """

    m = len(elem)

    A = (math.sqrt(5)-1)/2

    hash_function = lambda k : int(m*((k*A)% 1))

    dicc = d.Dictionary(hash_function, m)

    for key in elem:
        dicc.insert(dicc.D, key, str(key))

    count = 0

    for key in elem:
        if dicc.search(dicc.D, key) != None:
            dicc.delete(dicc.D, key)
            count += 1

    if count == m:
        return True
    else:
        return False


    # Ejercicio 6

def codigo_postal(dict, codigo):

    """
    La complejidad sera de O(1) ya que la longitud de los codigos esta definida, las operaciones son aritmeticas (O(1)) y las operaciones 
    de insercion y busqueda son O(1)
    """

    print(f"el codigo postal se insertara en la posicion {Codigo_postal_hash(codigo)}")
    dict.insert(dict.D, codigo, str(codigo))
    return dict.D

def Codigo_postal_hash(cp):

    ## Como la catidad de combinaciones es muy grande (Ronda los 40 billones) elejimos un nº primo muy grande
    m = 100003
    parte_num = int(cp[1:5])
    parte_string = cp[:1] + cp[5:]
    parte_string_ascii = sum(ord(c)*10**k for c,k in zip(parte_string, [4,3,2,1]))
    val = parte_num + parte_string_ascii
    hash_function = val % m
    
    return hash_function

    
    

    # Ejercicio 7

    """
    Complejidad de O(n) ya que itero una lista de longitud n, no encontre aplicacion efectiva en diccionarios
    """
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
    

"""
Complejidad de O(n), ya que itero solamente una lista de longitud n. Aun no logro implementar diccionarios de forma efectiva
"""

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

def isIn_v2(text, sub):
    
    """
    La complejidad sera de O(m+n) ya que depende de la longitud del texto insertado en la tabla (m) y la longitud del subtexto (n) 
    que van a ser iterados, en uno para la insercion en tabla, y el otro en la busqueda
    """


    aux = len(sub)
    dict = d.Dictionary(hash_text, 97)

    for i in range(len(text)):
        if i+aux <= len(text):
            new_char = text[i:i+aux]
            dict.insert(dict.D, new_char, new_char)
    found = dict.search(dict.D, sub)

    return found != None


    return False

def hash_text(text):

    char_ascii = 0

    for i in range(len(text)):
        char_ascii += ord(text[i])*10**i

    hash_function = char_ascii % 97

    return hash_function

def isSubConj(C, S): 

    """
    La complejidad sera de O(n), siendo n la longitud de la cadena mas larga
    """

    dict = d.Dictionary(None, 37) # elijo un numero primo 

    for i in C:
        dict.insert(dict.D, i, str(i)) 

    for i in S:

        aux = dict.search(dict.D, i)

        if aux != str(i):
            return False           

    return True





