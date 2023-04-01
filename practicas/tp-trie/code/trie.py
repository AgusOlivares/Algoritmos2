import linkedlist as ll

class Trie:
  root = None


class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False


def insert(T, element):

    if T.root is None:
        L = ll.LinkedList()
        node = TrieNode()
        node.key = L
        T.root = node
      
    lista = list(element)
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
  #node = TrieNode()
  #node1.parent = T.root
  #node1.key = palabra.pop()
