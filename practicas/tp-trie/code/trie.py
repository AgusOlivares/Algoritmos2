
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
                new_node.key = element[i]
                Flag = True
                current = new_node
            
            elif SearchL(current, element[i]) == current:        ## Debo buscar otra manera de comparar el elemento ya que si el search es "None", tira error
                if current.children != None:
                    current = current.children      ## Logre Insertar una parabla que tiene como prefijo otra, creo que se puede hacer mas eficiente
                elif current.nextNode != None:
                    current = current.nextNode
                else:
                    Flag = True ## Con Esta linea logre agregar palabras mas largas
                    continue

            else:  
                
                new_node = TrieNode()       ## Codigo parecido al del inicio la diferencia es que en la primera iteracion se va a conectar a la raiz                                     ## y luego voy a poder trabajar con el nodo que quiera
                new_node.parent = current
                current.children = new_node
                new_node.key = element[i]
                if element[i] == element[len(element)-1]:       ## Verifico si es el ultimo elemento de la palabra
                    new_node.isEndOfWord = True
                current = new_node
                



    




'''



    insertR(T.root, lista)


def insertR(Tnode, lista):

    if lista != []:
       
       new_node = TrieNode()
       Tnode.children = new_node
       new_node.parent = Tnode
       new_node.key = lista.pop(0) 
       return insertR(new_node, lista)
       
    else:
       Tnode.isEndOfWord = True

    return
  

'''
def SearchL(Node, element):

    while Node != None:
        if Node.key == element:
            return Node
        else:
            Node = Node.nextNode
    return None
    