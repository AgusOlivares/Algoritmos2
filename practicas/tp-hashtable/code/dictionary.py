class DictionaryNode:
    key = None
    value = None
    nextNode = None

   
        

def hash(A, k):
    #if         # Quiero poner condicion para utilizar distintas funciones de hash segun la situacion 
    return k % len(A)


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

# O(2n) == O(n)
def isConj(elem):
    return len(elem) == len(set(elem)) # O(n):longitud lista + O(n):set, recorre todos los elem y saca los repetidos 

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
            
            

# def Ordered       # Estaria bueno implementar una manera de insertar los elementos y que queden ordenados 