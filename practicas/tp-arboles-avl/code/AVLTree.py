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
        return 0
    node = ALVTree.root
   # Queremos actualizar el node.bf
    if node.leftnode is not None:
        height_left = balanceRecursive(node.leftnode)
    if node.rightnode is not None:
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

    altura = max(height_left, height_right)

    return altura + 1


def reBalance(AVLTree):

    calculateBalance(AVLTree)

    # Balanceo todo el arbol de una sola vez
    reBalance_R(AVLTree, AVLTree.root)

    return AVLTree


def reBalance_R(AVLTree, node):

    if node.leftnode is not None:
        reBalance_R(AVLTree, node.leftnode)

    # El arbol esta desbalanceado por derecha

    if node.bf < -1:

        if node.rightnode.bf > 0:

            node.parent.rightnode = rotateRight(AVLTree, node.rightnode)
            rotateLeft(AVLTree, node)
            calculateBalance(AVLTree)
        else:

            rotateLeft(AVLTree, node)
            calculateBalance(AVLTree)

    # El arbol esta desbalanceado por izquierda

    if node.bf > 1:

        if node.leftnode.bf < 0:
            node.parent.leftnode = rotateLeft(AVLTree, node.leftnode)
            rotateRight(AVLTree, node)
            calculateBalance(AVLTree)
        else:
            rotateRight(AVLTree, node)
            calculateBalance(AVLTree)

    if node.rightnode is not None:
        reBalance_R(AVLTree, node.rightnode)


# Tercera version
# Ahora balancea el arbol al insertar el nodo, pero hacia arriba, antes al reordenar todo perdia la complejidad O(n log n)
def insert_key(AVLTree, key):

    new_node = AVLNode()
    new_node.key = key
    current = AVLTree.root

    if current is None:
        AVLTree.root = new_node
        return new_node.key

    else:
        insertR(current, new_node)

    return


def insertR(current, new_node):

    if new_node.key < current.key:
        if current.leftnode is None:
            current.leftnode = new_node
            new_node.parent = current
            # Aca deberia volver a calcular el valor del padre
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


def insert(AVLTree, key):
    if AVLTree.root == None:
        return insert_key(AVLTree, key)

    new_node = AVLTree.root
    # Primero inserto el elemento
    new_node = insert_key(AVLTree, key)

    # Luego voy desde el nodo insertado hacia atras
    insert_recursive(AVLTree, new_node)
    return calculateBalance(AVLTree)


def insert_recursive(B, node):

    if node == None:
        return

    # Calculo el balance factor
    aux_avl = AVLTree()
    aux_avl.root = node
    calculateBalance(aux_avl)

    # Si esta desbalanceado entonces:
    if node.bf < -1 or node.bf > 1:
        # Separo en 2 casos:
        if node.bf < -1:
            # Caso 1: Guardo el padre y lo guardo en aux , luego en node retorno el nodo balanceado.
            # Luego vuelvo a asignar el hijo en el lado derecho (Por ser node.bf < -1)
            aux = node.parent
            B2 = AVLTree()
            B2.root = node
            node = reBalance(B2)
            aux.rightnode = node.root
            return aux.rightnode
        elif node.bf > 1:
            # Caso 2: Guardo el padre y lo guardo en aux , luego en node retorno el nodo balanceado.
            # Luego vuelvo a asignar el hijo en el lado izquierdo (Por ser node.bf > 1)
            aux = node.parent
            B2 = AVLTree()
            B2.root = node
            node = reBalance(B2)
            aux.leftnode = node.root
            return aux.leftnode
    else:
        # Si no esta desbalanceado me fijo en el parent
        return insert_recursive(B, node.parent)


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


def deleteR(B, node):

    # Caso 1: elimino una hoja
    if node.leftnode == None and node.rightnode == None:
        if node.parent.leftnode == node:
            node.parent.leftnode = None
            return node.key
        elif node.parent.rightnode == node:
            node.parent.rightnode = None
            return node.key

    # Caso 2: elimino un nodo con un hijo del lado izquierdo
    if node.leftnode != None and node.rightnode == None:
        if node.parent.leftnode != None and node.parent.leftnode == node:
            node.parent.leftnode = node.leftnode
            return node.key
        elif node.parent.rightnode != None and node.parent.rightnode == node:
            node.parent.rightnode = node.leftnode
            return node.key

    # Caso 3: elimino un nodo con un hijo del lado derecho
    if node.rightnode != None and node.leftnode == None:
        if node.parent.rightnode != None and node.parent.rightnode == node:
            node.parent.rightnode = node.rightnode
            return node.key
        elif node.parent.leftnode != None and node.parent.leftnode == node:
            node.parent.leftnode = node.rightnode
            return node.key

    # Caso 4: eliminar un nodo con dos hijos
    # En este caso, se reemplaza el nodo a eliminar por el nodo sucesor en orden, que es el nodo más pequeño en su subárbol derecho
    successor = get_successor(node.rightnode)
    node.key = successor.key
    deleteR(B, successor)


#def mayor_menores(node):

    #if node.rightnode != None:
    #    currentNode = mayor_menores(node.rightnode)
    #    if currentNode != None:
    #        return currentNode
    #else:
    #    return node


def get_successor(node):
   # Se encuentra el nodo sucesor en orden del arbol, nodo mas pequeño en subarbol derecho del nodo dado
    current = node
    while current.leftnode is not None:
        current = current.leftnode
    return current
