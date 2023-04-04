
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
        node.key = None
        T.root = node
      
    lista = list(element)

    if SerchL(T.root.children, lista[0]) == False:      ## Intento implementar la linkedlist agregando un parametro extra en el TrieNode para que haga una lista dentro del mismo nodo
                                                        ## Va a ser mas o menos como que me puedo mover para arriba, para abajo y tambien para la Izq dentro del mismo nodo
       
        if T.root.children is None:
          
            node = TrieNode()







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
  

def SerchL(Node, element):

    while Node != None:
        if Node.key == element:
            return True
        else:
            Node = Node.nextNode
    return False
    