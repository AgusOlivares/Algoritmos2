class Trie:
  root = None


class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False


def insert(T, element):

    if T.root is None:
        node = TrieNode()
        T.root = node
    lista = list(element)
    insertR(T.root, lista, 0)


def insertR(Tnode, lista, i):

    if lista is not []:
       i = 0
       new_node = TrieNode()
       Tnode.children = new_node
       new_node.parent = Tnode
       new_node.key = lista.pop([i]) 
       insertR(new_node, lista, i+1)
    else:
       Tnode.isEndOfWord = True


  #node = TrieNode()
  #node1.parent = T.root
  #node1.key = palabra.pop()
