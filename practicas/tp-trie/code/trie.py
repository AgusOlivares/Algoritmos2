
class Trie:
  root = None


class TrieNode:
  parent = None
  nextNode = None
  children = None
  key = None
  isEndOfWord = False

class linkedlist:
    head = None






  

def insert(T, element):

    if T.root is None:
        node = TrieNode()
        T.root = node
        
    current = T.root.children       ## Elijo el nodo "Head" de la lista, si es que existe
    Flag = False

    if current is None:
        new_node = TrieNode()
        new_node.parent = T.root
        T.root.children = new_node 
        current = new_node

    for i in range(len(element)):

        if current.key == None:
            current.key = element[i]
            Flag = True
            
        else:
            if SearchL(current, element[i]) == None and Flag == False: 
            
                new_node = TrieNode()       ## Se complica al insertar mas de dos palablar porque empiezan a pisar el campo nextNode y no se conectan de forma efectiva
                new_node.nextNode = current.nextNode        ## Al agregar esta linea logre insertar mas de 2 palabras a la primera fila    
                current.nextNode = new_node
                new_node.key = element[i]           ## Me falta asignar bien los parents aca
                Flag = True
                # Experimental
                new_node.parent = current.parent
                ##
                current = new_node
            
            elif SearchL(current, element[i]) != None: 
                current = SearchL(current, element[i])       ## Debo buscar otra manera de comparar el elemento ya que si el search es "None", tira error
                ## Al insertar la palabra mamarracho falla por la iteracion numero 5, ya que al repetir el valor del nodo, falla en...
                if current.children != None:  ## ... Esta parte
                    
                    current = current.children      ## Logre Insertar una parabla que tiene como prefijo otra, creo que se puede hacer mas eficiente
                else:
                    Flag = True ## Con Esta linea logre agregar palabras mas largas
                    continue

            else:  
                
                new_node = TrieNode()       ## Codigo parecido al del inicio la diferencia es que en la primera iteracion se va a conectar a la raiz                                     ## y luego voy a poder trabajar con el nodo que quiera
                new_node.parent = current
                current.children = new_node
                new_node.key = element[i]
                current = new_node
            
            if element[i] == element[len(element)-1] and i == len(element)-1:       ## Verifico si es el ultimo elemento de la palabra
                if current.key != element[i]:
                    current.parent.isEndOfWord = True
                else:    
                    current.isEndOfWord = True
                
   


def SearchL(Node, element):

    while Node != None:
        if Node.key == element:
            return Node
        else:
            Node = Node.nextNode
    return None
    
def search(T, element):

    current = T.root.children
    return searchR(current, element)

def searchR(current, element):

    if current == None:
        return False
    
    pos = SearchL(current, element[0])
    aux = pos != None

    if aux == False:
        return False
    
    if len(element) == 1 and pos.isEndOfWord == True:
        return True
    element = element[1:]

    return searchR(pos.children, element)


def delete(T, element):

    current = T.root.children

    if search(T, element) == False:
        return False
    
    EndWord = toEndofWord(current, element)


    # Funciona Caso 0: Palabra dentro de palabra

    if current.children != None and current.isEndOfWord is True:
        current.isEndOfWord = False
        return True
    
    # Funciona Caso 1: Nodo final solitario
    
    if current.children is None and current.isEndOfWord is True:
        if current.nextNode is None:
            
            current.parent.children = None
        elif current.nextNode is not None:
            aux = current
            current.parent.children = aux.nextNode
   



            

    
     


def toEndofWord(List, element):
    
    current = SearchL(List, element[0])

    if current != None and current.children != None:
        current = current.children
    if current.key == element[len(element)-1] and current.isEndOfWord == True:
        return current
    element = element[1:]
    return toEndofWord(current, element)


def PrintChain(T, p, n):

    if T.root == None:
        return None
    
    last_node = toEndofPattern(T.root.children, p)

    if last_node == None:
        return None
    
    n = n - len(p)
    ListaPalabras = []
    current = last_node
    aux = n


    ## He posicionado mal los marcadores, imaginate que te estas moviendo por algo parecido a una matriz (No es una matriz, ojo)
    ## Tengo que cambiarlos por algo mas facil de manejar que un while, intentar con un "for"
    ## El caso que se me complica es revisar los nodos en forma de "Escalera"
    while n > 0:
        while aux > 0:
            if current.nextNode != None:
                current = current.children


            aux -= 1
        CheckEnd(last_node, ListaPalabras)    

        if last_node.children != None:
            last_node = last_node.children
            current = last_node

        n -= 1
    CheckEnd(current, ListaPalabras)

    #CheckEnd(last_node, ListaPalabras)
    return ListaPalabras


    


def CheckEnd(List, ListaPalabras):       ## Checkea que alguno de los elementos de la lista tenga EndOfWord = True
    if List == None:
        return 
    if List.isEndOfWord == True:
        aux = ''    
        palabra = AlmacenarPalabra(List, aux)
        ListaPalabras.append(palabra)

    CheckEnd(List.nextNode, ListaPalabras)
    return ListaPalabras

def AlmacenarPalabra(List, aux):        ## Almacena una palabra accediendo a los keys de los parents

    if List.key == None:
        return aux
    aux = List.key + aux
    return AlmacenarPalabra(List.parent, aux)

def toEndofPattern(List, element):
    
    current = SearchL(List, element[0])

    if current != None:
        current = current.children
    else:
        return None
    if current.key == element[len(element)-1]:
        return current
    element = element[1:]
    return toEndofPattern(current, element)


'''

'''


    
