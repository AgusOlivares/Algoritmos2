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

  if raizNueva.leftnode is None:
   raizNueva.leftnode = raizVieja
  else:
    raizNueva.leftnode = raizVieja
    raizVieja.rightnode = aux

  return raizNueva

def rotateRight(Tree, avlnode):

  raizVieja = avlnode
  Tree.root = avlnode.leftnode
  raizNueva = Tree.root
  aux = Tree.root.rightnode

  if raizNueva.rightnode is None:
   raizNueva.rightnode = raizVieja
  else:
    raizNueva.rightnode = raizVieja
    raizVieja.leftnode = aux

  return raizNueva
  

def calculateBalance(ALVTree):
     node = AVLNode()
     node = ALVTree.root
     #Queremos actualizar el node.bf
     height_left = balanceRecursive(node.leftnode)
     height_right = balanceRecursive(node.rightnode)
     bf = height_left - height_right
     node.bf = bf

     return node
     

def balanceRecursive(node):
     
     if node == None:
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
  ## 
  if node.bf != 0 and node.bf != 1 and node.bf != -1:
    if node.bf < -1:
      #if node.rightnode.bf < -1:
      rotateLeft(AVLTree, node)
    if node.bf > 1:
      rotateRight(AVLTree, node)
      
  reBalance_R(AVLTree, node.leftnode)
  reBalance_R(AVLTree, node.rightnode)

  return node

     

def reBalance_R(AVLTree, node):

  if node == None:
    return

  if node.bf != 0 and node.bf != 1 and node.bf != -1:
    if node.bf < -1:
      rotateLeft(AVLTree, node)
    if node.bf > 1:
      rotateRight(AVLTree, node)
  
  reBalance_R(node.leftnode)
  reBalance_R(node.rightnode)

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



