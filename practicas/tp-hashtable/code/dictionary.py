class DictionaryNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        

class Dictionary:
    def __init__(self, hash_function = None, longitud = 13):
        self.D = [None] * longitud

        if hash_function != None:
            self.hash_function = hash_function
        else: 
            self.hash_function = lambda k: k % longitud


    # def Ordered       # Estaria bueno implementar una manera de insertar los elementos en la tabla y que queden ordenados 
    def insert(self, D, k, val):

        new_k = self.hash_function(k)


        if D[new_k] is None:
            node = DictionaryNode(k, val)
            D[new_k] = []
            D[new_k].append(node)
        else:
            
            
            node = DictionaryNode(k, val)
            
            if search_key(k, D[new_k]) != None:     # Reviso que la key no exista ya asociada a un valor
                return D
            if search_inList(val, D[new_k]) == False:   # Reviso que el valor no exista ya asociado a una key
                D[new_k].append(node)
            
        return D

    def search(self, D, k):

        new_k = self.hash_function(k)

        if D[new_k] is None:
            return D
        else:
            list = D[new_k]
            pos = search_key(k, list)
            if pos == None:
                return None
            else:
                return list[pos].value

    def delete(self, D, k):

        new_k = self.hash_function(k)

        if D[new_k] is None:
            return D
        else:

            list = D[new_k]
            pos = search_key(k, list)

            if pos is None:
                return D
            else: 
                list.pop(pos)
                return D

def search_inList(element, list):

    for i in range(len(list)):
        if list[i] is not None:
            if element == list[i].value:
                return True
    return False


def search_key(key , list):

    for i in range(len(list)):
        if list[i] != None:
            if key == list[i].key:
                return i
    return None
    

