from algo1 import *
from linkedlist import *
from myqueue import enqueue, dequeue


class BinaryTree:
    root = None


class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None


def search(B, element):
    current = searchR(B.root, element)
    if current == None:
        return None
    else:
        return current.key

def searchR(current, element):

    if current == None:
        return None
    if current.value == element:
        return current

    leftNode = searchR(current.leftnode, element)
    if leftNode != None:

        return leftNode

    rightNode = searchR(current.rightnode, element)
    if rightNode != None:

        return rightNode


def insert(B, element, key):
    newNode = BinaryTreeNode()
    newNode.value = element
    newNode.key = key
    current = B.root

    if current != None:
        return insertR(current, newNode)
    else:
        B.root = newNode
        return newNode.key


def insertR(current, newNode):

    if newNode.key < current.key:
        if current.leftnode == None:
            current.leftnode = newNode
            newNode.parent = current
            return newNode.key
        else:
            return insertR(current.leftnode, newNode)
    elif newNode.key > current.key:
        if current.rightnode == None:
            current.rightnode = newNode
            newNode.parent = current
            return newNode.key
        else:
            return insertR(current.rightnode, newNode)
    else:
        return None


def access(B, key):
    current = accessNode(B.root, key)

    if current == None:
        return None
    else:
        return current.value

def accessNode(Node, key):

    if Node == None:
        return None
    elif Node.key == key:
        return Node

    LeftNode = accessNode(Node.leftnode, key)
    if LeftNode != None:
        return LeftNode

    RightNode = accessNode(Node.rightnode, key)
    if RightNode != None:
        return RightNode


def update(B, element, key):

    Node = B.root
    current = searchNode(Node, key)

    if current != None:
        current.value = element
        return current.key


def searchNode(current, key):

    if current == None:
        return None
    if current.key == key:
        return current

    leftNode = searchNode(current.leftnode, key)
    if leftNode != None:

        return leftNode

    rightNode = searchNode(current.rightnode, key)
    if rightNode != None:

        return rightNode


'''
En el delete solo he probado el caso base (nodo a eliminar es nodo hoja), aun falta hacer el caso general y poder reacomodar el arbol luego


def delete(B, element):

    current = B.root
    currKey = search(B, element)

    Nodo_elim = searchNode(current, currKey)

    ## Caso 1 (Hoja)
    if Nodo_elim != None:
        if Nodo_elim.leftnode == None and Nodo_elim.rightnode == None:
            padre = Nodo_elim.parent

            if padre.leftnode == Nodo_elim:
                padre.leftnode = None
            else:
                padre.rightnode = None
            Nodo_elim.parent = None
            return Nodo_elim.key
'''


def delete(B, element):
    node = searchR(B.root, element)

    if node == None:
        return None
    else:
        return deleteR(B, node)


def deleteR(B, node):

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


def deleteKey(B, key):
    node = searchR(B.root, key)

    if node == None:
        return None
    else:
        return deleteR(B, node)


def traverseInPreOrder(B):
    list = LinkedList()
    current = B.root

    if B.root != None:
        add(list, current)
        ListFill(current.leftnode, list)
        ListFill(current.rightnode, list)
        return Invertir(list)
    else:
        return None

def ListFill(Node, L):
    if Node != None:
        if Search(L, Node) == None:
            add(L, Node)
        if Node.leftnode != None and Search(L, Node.leftnode) == None:
            ListFill(Node.leftnode, L)
        else:
            if Node.rightnode != None and Search(L, Node.rightnode) == None:
                ListFill(Node.rightnode, L)
            elif Node.rightnode == None:
                Node = Node.parent
                ListFill(Node, L)
    else:
        return L

def traverseInOrder(B):
    L = LinkedList()
    traverseInOrderR(B.root, L)
    return Invertir(L)


def traverseInOrderR(node, L):
    if node != None:
        traverseInOrderR(node.leftnode, L)
        add(L, node.value)
        traverseInOrderR(node.rightnode, L)


def traverseInPostOrder(B):
    L = LinkedList()
    traverseInPostOrderR(B.root, L)
    return Invertir(L)


def traverseInPostOrderR(node, L):
    if node != None:
        traverseInPostOrderR(node.leftnode, L)
        traverseInPostOrderR(node.rightnode, L)
        add(L, node.value)


def traverseBreadFirst(B):
    queue = LinkedList()
    valuesQueue = LinkedList()
    enqueue(queue, B.root)
    while queue.head != None:
        node = dequeue(queue)
        enqueue(valuesQueue, node.value)

        if node.leftnode != None:
            enqueue(queue, node.leftnode)
        if node.rightnode != None:
            enqueue(queue, node.rightnode)
    return Invertir(valuesQueue)
