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
    


def search(AVLTree, key):
    current = searchR(AVLTree.root, key)
    if current == None:
        return None
    else:
        return current

def searchR(node, key):

    if node == None:
        return None
    if node.key == key:
        return node

    leftNode = searchR(node.leftnode, key)
    if leftNode != None:

        return leftNode

    rightNode = searchR(node.rightnode, key)
    if rightNode != None:

        return rightNode

  # Implementacion delete

def delete(AVLTree, key):
  node = searchR(AVLTree.root, key)
  if node == None:
      return None
  else:
      deleteR(AVLTree, node)
      calculateBalance(AVLTree)
      reBalance(AVLTree)
  
def deleteR(AVLTree, node):

    #Caso 1: elimino una hoja
    if node.leftnode == None and node.rightnode == None:
        if node.parent.leftnode == node:
            node.parent.leftnode = None
            return node.key
        elif node.parent.rightnode == node:
            node.parent.rightnode = None
            return node.key

    #Caso 2: elimino un nodo con un hijo del lado izquierdo
    if node.leftnode != None and node.rightnode == None:
        if node.parent.leftnode != None and node.parent.leftnode == node:
            node.parent.leftnode = node.leftnode
            return node.key
        elif node.parent.rightnode != None and node.parent.rightnode == node:
            node.parent.rightnode = node.leftnode
            return node.key

    #Caso 3: elimino un nodo con un hijo del lado derecho
    if node.rightnode != None and node.leftnode == None:
        if node.parent.rightnode != None and node.parent.rightnode == node:
            node.parent.rightnode = node.rightnode
            return node.key
        elif node.parent.leftnode != None and node.parent.leftnode == node:
            node.parent.leftnode = node.rightnode
            return node.key

    #Caso 4: Elimino un nodo que tiene 2 hijos
    mayor = mayor_menores(node.leftnode)
    aux = node.key
    node.value = mayor.value
    node.key = mayor.key

    mayor.parent.rightnode = mayor.leftnode
    return aux

def mayor_menores(node):

    if node.rightnode != None:
        currentNode = mayor_menores(node.rightnode)
        if currentNode != None:
            return currentNode
    else:
        return node