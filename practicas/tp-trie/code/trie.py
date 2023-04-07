
class Trie:
  root = None


class TrieNode:
  parent = None
  nextNode = None
  children = None
  key = None
  isEndOfWord = False








  

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


    return deleteR(current, element)

def deleteR(current, element):

    current = toEndofWord(current, element)

    if current.children != None and current.isEndOfWord == True:
        current.isEndOfWord = False
        return True
    
     


def toEndofWord(List, element):
    
    current = SearchL(List, element[0])

    if current != None and current.children != None:
        current = current.children
    if current.key == element[len(element)-1] and current.isEndOfWord == True:
        return current
    element = element[1:]
    return toEndofWord(current, element)





    
