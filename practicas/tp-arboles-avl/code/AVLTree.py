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


  ## Desconecto la vieja raiz del nodo superior en caso de tenerlo ··· solucion: me falto desconectar al padre del hijo
  ## por lo que si bien la raiz vieja se desconecto de su nodo padre, el padre sigue conectado a la raiz vieja
  
  raizNueva.parent = raizVieja.parent
  raizVieja.parent.leftnode = raizNueva
  raizVieja.parent = raizNueva 
  
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



  ## Desconecto la vieja raiz del nodo superior en caso de tenerlo
  ### Me falta desconectar el nodo superior del left o right node correspondiente
  
  
  raizNueva.parent = raizVieja.parent
  raizVieja.parent.rightnode = raizNueva 
  raizVieja.parent = raizNueva 

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

  # Modificacion: hago que reBalance_R reciba un parametro en vez de 2

  # El arbol esta desbalanceado por derecha
  if node.bf < -1:
    reBalance_R(node.rightnode)
    
  # El arbol esta desbalanceado por izquierda
  if node.bf > 1:
    reBalance_R(node.leftnode)
    
    
  return node

    

def reBalance_R(node):

  if node is None:
    return
  
  # Modificacion : En la version anterior recibia el arbol original, falla: modificaba la raiz del arbol original...
  # ... Ahora al tener un arbol auxiliar, modifico al subarbol
  
  arbol_aux = AVLTree
  arbol_aux.root = node

  if node.bf < 0: 
    if node.rightnode.bf > 0 :
      
      rotateRight(arbol_aux, node.rightnode)
      rotateLeft(arbol_aux, node) ## de aca elimine los .parent
    else:
      rotateLeft(arbol_aux, node)

  if node.bf > 0:
    if node.leftnode.bf > 1 :
      rotateLeft(arbol_aux, node.leftnode)
      rotateRight(arbol_aux, node) ## de aca elimine los .parent
    else:
      rotateRight(arbol_aux, node)


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



