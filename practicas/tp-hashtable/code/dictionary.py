class DictionaryNode:
    key = None
    value = None
    nextNode = None

   
        

def hash(A, k):
    #if         # Quiero poner condicion para utilizar distintas funciones de hash segun la situacion 
    return k % len(A)


def insert(D, k, val):

    pos = hash(D,k)

    if D[pos] is None or D[pos] == 0:
        node = DictionaryNode()
        node.value = val
        node.key = k
        D[pos] = node
    else:
        node = DictionaryNode()
        node.value = val
        node.key = k
        node.nextNode = D[pos]
        D[pos] = node
        
    return D

def search(D, key):

    pos = hash(D, key)

    if D[pos] is None:
        return None
    else:
        node = D[pos]
        while node.nextNode is not None:
            if node.nextNode.key is not key:
                node = node.nextNode
            else:
                return node.key
        return None    

def delete(D, key):

    if search(D, key) is None:
        return None
    else:
        pos = hash(D, key)
        node = D[pos]

        if D[pos].key == key:
            D[pos] = node.nextNode
        else:
            while node.nextNode is not None:

                if node.nextNode.key != key:
                    node = node.nextNode
                else:
                    if node.nextNode.nextNode is None:
                        node.nextNode = None
                    else:
                        node.nextNode = node.nextNode.nextNode
            return D





# def Ordered       # Estaria bueno implementar una manera de insertar los elementos y que queden ordenados 