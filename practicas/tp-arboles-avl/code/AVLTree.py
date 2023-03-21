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
  aux = Tree.root.leftnode 

  raizNueva.leftnode = raizVieja
  raizNueva.parent = raizVieja.parent

  raizVieja.rightnode = None
  raizVieja.parent = raizNueva
  


  if aux is not None:
    raizVieja.rightnode = aux
    aux.parent = raizVieja

  return raizNueva

def rotateRight(Tree, avlnode):

  raizVieja = avlnode
  Tree.root = avlnode.leftnode
  raizNueva = Tree.root
  aux = Tree.root.rightnode

  raizNueva.rightnode = raizVieja
  raizNueva.parent = raizVieja.parent

  raizVieja.leftnode = None
  raizVieja.parent = raizNueva
  


  if aux is not None:
    raizVieja.leftnode = aux
    aux.parent = raizVieja

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
   
  
  calculateBalance(AVLTree)

  # Balanceo todo el arbol de una sola vez
  AVLTree = reBalance_R(AVLTree ,AVLTree.root)
    
    
  return AVLTree

    

def reBalance_R(AVLTree, node):

  if node.leftnode is not None:
    reBalance_R(AVLTree, node.leftnode)

  
  # El arbol esta desbalanceado por derecha

  if node.bf < -1: 

    if node.rightnode.bf > 0 :
      
      
      rotateRight(AVLTree, node.rightnode)
      rotateLeft(AVLTree, node) 
      calculateBalance(AVLTree)
    else:
      
      rotateLeft(AVLTree, node)
      calculateBalance(AVLTree)
    
  
  # El arbol esta desbalanceado por izquierda

  if node.bf > 1:

    if node.leftnode.bf < 0 :
      rotateLeft(AVLTree, node.leftnode)
      rotateRight(AVLTree, node) 
      calculateBalance(AVLTree)
    else:
      rotateRight(AVLTree, node)
      calculateBalance(AVLTree)

  if node.rightnode is not None:
    reBalance_R(AVLTree, node.rightnode)



# Segunda Version
## Ahora balancea el arbol al insertar el nodo
def insert(AVLTree, key):

  new_node = AVLNode()
  new_node.key = key
  current = AVLTree.root

  if current is None:
    AVLTree.root = new_node
    return new_node
  
  else:
    insertR(current, new_node)

  calculateBalance(AVLTree)
  reBalance(AVLTree)
  return
    
      
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