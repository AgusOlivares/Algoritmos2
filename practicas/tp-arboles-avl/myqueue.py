from linkedlist import *
from algo1 import *


def enqueue(Q, element):
    add(Q, element)


def dequeue(Q):
    node = Q.head
    if node == None:
        return None
    elif node.nextNode != None:
        while node != None:
            if node.nextNode.nextNode == None:
                valor = node.nextNode.value
                break
            else:
                node = node.nextNode
        node.nextNode = None
        return valor
    else:
        value = node.value
        Q.head = None
        return value


def printlist(Q):

    pointer = Q.head

    if pointer == None:
        return None
    else:
        while pointer != None:
            print(pointer.value, end="  |  ")

            pointer = pointer.nextNode
    print()
    return
