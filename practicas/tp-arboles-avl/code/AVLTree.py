class AVLTree:
  root = None


class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None


def rotateLeft(Tree, avlnode):

  raizVieja = avlnode
  Tree.root = avlnode.rightnode
  raizNueva = Tree.root

  raizNueva.parent = avlnode.parent
  raizNueva.parent.rightnode = raizNueva
  raizVieja.parent = raizNueva
  # no desconecte la raiz vieja de la nueva raiz
  raizVieja.rightnode = None

  aux = raizNueva.leftnode 
  raizNueva.leftnode = raizVieja

  if aux is not None:
    raizVieja.rightnode = aux

  return raizNueva

def rotateRight(Tree, avlnode):

  raizVieja = avlnode
  Tree.root = avlnode.leftnode
  raizNueva = Tree.root

  raizNueva.parent = avlnode.parent
  raizNueva.parent.leftnode = raizNueva
  raizVieja.parent = raizNueva
  # no desconecte la raiz vieja de la nueva raiz
  raizVieja.leftnode = None

  aux = raizNueva.rightnode
  raizNueva.rightnode = raizVieja

  if aux is not None:
    raizVieja.leftnode = aux

  return raizNueva
  

def calculateBalance(ALVTree):
     
     if ALVTree is None:
       return 
     node = AVLNode()
     node = ALVTree.root
     #Queremos actualizar el node.bf
     height_left = balanceRecursive(node.leftnode)
     height_right = balanceRecursive(node.rightnode)
     bf = height_left - height_right
     node.bf = bf

     return ALVTree
     

def balanceRecursive(node):
     
     if node is None:
          return 0
     
     height_left = balanceRecursive(node.leftnode)
     height_right = balanceRecursive(node.rightnode)

     bf = height_left - height_right
     node.bf = bf

     altura = max(height_left , height_right)

     return 1 + altura

def reBalance(AVLTree):
   
  
  node = AVLNode()
  node = AVLTree.root
  calculateBalance(AVLTree)
  ### Problema: no se rebalancea la raiz

  # Balanceo tanto la rama izquierda como la derecha del arbol
  node.rightnode = reBalance_R(node.rightnode)
    
  node.leftnode =reBalance_R(node.leftnode)
    
    
  return AVLTree

   

def reBalance_R(node):

  if node is None:
    return

  arbol = AVLTree()
  arbol.root = node

  # Rebalanceo los subarboles del nodo ingresado de forma recursiva
  # de esta manera busco el nodo desbalanceado

  node.rightnode = reBalance_R(node.rightnode)
  node.leftnode = reBalance_R(node.leftnode)

  
  
  # El arbol esta desbalanceado por derecha

  if node.bf < 0: 

    if node.rightnode.bf > 0 :
      
      # puse arbol en vez de avltree
      rotateRight(arbol, node.rightnode)
      rotateLeft(arbol, node) 
      calculateBalance(arbol)
    else:
      # deberia poner arbol?
      #puse arbol en vez de avltree
      rotateLeft(arbol, node)
      calculateBalance(arbol)
    
  
  # El arbol esta desbalanceado por izquierda

  if node.bf > 0:

    if node.leftnode.bf < 0 :
      # puse arbol en vez de avltree
      rotateLeft(arbol, node.leftnode)
      rotateRight(arbol, node) 
      calculateBalance(arbol)
    else:
      # puse arbol en vez de avltree
      rotateRight(arbol, node)
      calculateBalance(arbol)


  return node


## Primera Version
## Implemento insert basico para crear el arbol
## Aun no inserta el nodo balanceando el arbol
def insert(AVLTree, key):

  new_node = AVLNode()
  new_node.key = key
  current = AVLTree.root

  if current is None:
    AVLTree.root = new_node
    return new_node
  
  else:
    return insertR(current, new_node)

    
      
def insertR(current, new_node):

  if new_node.key < current.key:
    if current.leftnode is None:
      current.leftnode = new_node
      new_node.parent = current
      return new_node
    else:
      return insertR(current.leftnode, new_node)
      
  if new_node.key > current.key:
    if current.rightnode is None:
      current.rightnode = new_node
      new_node.parent = current
      return new_node
    else:
      return insertR(current.rightnode, new_node)