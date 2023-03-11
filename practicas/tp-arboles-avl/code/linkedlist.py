class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


## O(1)
def add(L, element):

    ## Agrego un valor en forma de nuevo nodo en la lista enlazada

    current = L.head  ## pointer
    newNode = Node()
    newNode.value = element

    if L.head != None:

        newNode.nextNode = current
        L.head = newNode

    else:
        L.head = newNode


## O(n)
def Search(L, element):  ##le cambiaste la s por S, el arbol no te dejaba

    ## Busca un elemento en la lista y devuelve la posicion donde se encuentra

    current = L.head  ## pointer
    contador = 0

    while current != None:

        if current.value == element:
            return contador

        current = current.nextNode
        contador += 1
    return


## O(n)
def insert(L, element, position):

    # Inserta un elemento en la posicion indicada, desplazando el resto a la derecha, la lista se alarga

    current = L.head  ## pointer
    contador = 0

    if position == 0:
        add(L, element)
        return contador
    if position > 0:

        if current == None:
            return
        newNode = Node()
        newNode.value = element

        while current.nextNode != None:
            if contador + 1 != position:
                current = current.nextNode
                contador += 1
            else:
                newNode.nextNode = current.nextNode
                current.nextNode = newNode
                return position
        current.nextNode = newNode
        return contador + 1
    return


## O(n)
def length(L):
    ## devuelve la cantidad de elementos que posee una lista
    current = L.head  ## pointer
    contador = 0

    while current != None:
        current = current.nextNode
        contador += 1

    return contador


## O(n^2)
def Delete(L, element):

    ## Elimina un objeto de la lista, la lista se acorta

    current = L.head
    contador = Search(L, element)

    if contador == None:
        return None
    if contador == 0:
        L.head = current.nextNode
        return contador
    else:
        for i in range(0, contador - 1):
            current = current.nextNode

        current.nextNode = current.nextNode.nextNode
    return contador


## O(n)
def access(L, position):

    #Devuelve el valor de una posicion determinada de la lista

    current = L.head

    if position > 0:
        for i in range(1, position + 1):
            if current == None: return
            current = current.nextNode

        return current.value
    return


## O(n)
def update(L, element, position):

    # Actualiza el valor de una posicion determinada
    current = L.head

    if position >= 0:
        for i in range(0, position):

            current = current.nextNode
            if current == None:
                return

        current.value = element

        return position

    return


def printlist(L):

    pointer = L.head

    if pointer == None:
        return print(None)
    else:
        while pointer != None:
            print(pointer.value, end="  |  ")

            pointer = pointer.nextNode
    print("")
    return


######### COMPLETAR ESTA PARTE DEL EJERCICIO 4


def previousNode(L, position):

    pointer = L.head
    contador = 0

    while contador < position - 1:
        pointer = pointer.nextNode
        contador += 1
    return pointer


def move(L, position_O, position_D):

    if position_O == position_D: return
    elif position_O:
        ## head es la posicion de origen
        originalNode = L.head

        L.head = L.head.nextNode
        previousDest = previousNode(L, position_D)
        originalNode.nextNode = previousDest.nextNode


def Invertir(L):
    L_Aux = LinkedList()
    len = length(L)
    pointer = L.head

    for i in range(len):
        len -= 1
        add(L_Aux, pointer.value)
        pointer = pointer.nextNode
    return L_Aux
