from linkedlist import *
from algo1 import *


def push(S, element):
    add(S, element)
    return


def pop(S):

    if S.head != None:
        valor = S.head.value
        Delete(S, valor)
    else:
        return None

    return valor
