
class GraphNode:

    def __init__(self, key = None, color = "white") -> None:
        self.key = key 
        self.color = color
        self.connect = [] # funcionaria agregar un set() y en vez de append() un add()?

class Graph:

    def __init__(self, n) -> None: 
        
        ## nodes in graph
        self._n = n    

        ## Test, data is stored in dictionary
        self._data : dict[list[GraphNode]] = {}

    @property
    def n(self):
        return self._n

        
    def createGraph(self, vertices, aristas):

        for vertex in vertices:
            self.insert(vertex)
            

        for (vertice0, vertice1) in aristas:
            self.link(vertice0, vertice1)
            
        return 
        
        
    def link(self, vertice0, vertice1):

        if vertice0 not in self._data or vertice1 not in self._data:
            raise Exception("One or both vertices not in graph")
        
        node0 = self._data[vertice0]
        node1 = self._data[vertice1]

        
        if vertice1 in node0.connect:
            raise Exception("Link already exist in graph")

        if vertice0 in node1.connect:
            raise Exception("Link already exist in graph")
        

        if vertice0 == vertice1: node0.connect.append(vertice1); return


        node0.connect.append(vertice1)
        node1.connect.append(vertice0)
        return

    def insert(self, vertice): 

        if vertice in self._data:
            raise Exception("Node already exist in the graph")
        
        if vertice not in self.n:
            self.n.append(vertice)
        
        node = GraphNode(vertice)

        # Insert vertex value as key and create a graphnode in dictionary[key]
        self._data[vertice] = node


    def printGraph(self):
        for vertice in sorted(self._data.keys()):
            node = self._data[vertice]
            conexiones = sorted(node.connect)
            print(f"{vertice}: {conexiones}")

    def existPath(self, v0, v1):
        ## Verifico que los nodos ingresados existan dentro del grafo
        if v0 not in self._data or v1 not in self._data:
            raise Exception("One or both vs not in graph")
        
        ## Verifico si son iguales 
        if v0 == v1: return True
        
        visited = set()
        queue = [v0]

        ## Busco mientras haya elementos en la cola
        while queue:

            aux = queue.pop(0)

            # Si el vertice no ha sido visitado, lo agrego al conjunto
            if aux not in visited:
                visited.add(aux)
                # Recorro los vertices adyacentes del vertice actual
                for adjacent in self._data[aux].connect:
                    
                    # Si encuentro el vertice, retorno
                    if adjacent == v1:
                        return True
                    
                    queue.append(adjacent)
                
        return False
    


    def isConnected(self):   


        nodos = self.n.copy()

        aux = nodos.pop()

        for nodo in nodos:
            if self.existPath(aux, nodo) != True: return False

        return True  


    def isTree(self):
        
        if self.isConnected() != True: return False

        if self.existCycle(): return False ## REVISAR ESTA FUNCION
        """
        Al empezar a revisar la lista, inevitablemente al empezar a ver las listas de adyacencia
        y empezar a encolar los elementos pueden llegar a repetirse los valores, encontrar una solucion a eso
        """

        print("hola")

        return True



    def existCycle(self): ## REVISAR, CON EL EJEMPLO DADO DEBERIA DAR FALSE
        
        nodos = self.n.copy()
        v0 = nodos.pop(0)

        visited = set()
        queue = [v0]

        while queue:

            if queue.count(queue[0]) > 1:
                return True

            aux = queue.pop(0)

            if aux not in visited:
                visited.add(aux)

                

                for adjacent in self._data[aux].connect:
                    queue.append(adjacent)
                
        

    def isComplete(self):

        if len(self._data[1].connect) != len(self.n)-1:
            return False
        return True
    


                    
                

            

        



        

        

        

        
        
        




