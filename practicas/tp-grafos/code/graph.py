
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


    def isTree(self, graph):

        def visit_TreeNode(graph, node, visited_key, inmediate_parent):

            if node.key in visited_key:
                return True
            

            visited_key.add(node.key)

            for adj_node in graph._data[node.key].connect:
                
                if adj_node in visited_key:
                    
                    if graph._data[adj_node] != inmediate_parent: return False

                tree = visit_TreeNode(graph, graph._data[adj_node], visited_key, node)
                if not tree: return False
            return True

        
        if self.isConnected() == False: return False


        visited_key = set()
        components = 0

        for node in graph._data:

           if node not in visited_key:
               
                if components == 1:
                    return False    

                components += 1
                tree = visit_TreeNode(graph, graph._data[node], visited_key, None)
        if not tree: return False
        return True
                    
                
        

    def isComplete(self):

        aux = self.n.copy()

        aux2 = aux.pop()

        if len(self._data[aux2].connect) != len(self.n)-1:
            return False
        return True
    

    def convertTree(self, graph):

        if graph.isTree(graph): return graph

        aux = graph.n.copy()
        key = aux.pop()

        visited = set()
        edges = []
        queue =[(key, None)]

        while queue:
            ## Aux va a ser el nodo de referencia "head"
            node, parent = queue.pop(0) 

            if node not in visited: 
                visited.add(node)

                if parent is not None:
                    edges.append((parent, node))
                
                for adj in graph._data[node].connect:
                    if adj not in visited:
                        queue.append((adj, node))
        
        new_graph = Graph(self.n)
        new_graph.createGraph(self.n, edges)

        return new_graph
    

    def countConnections(self, graph):
        
        if self.isConnected(): return 1

        count = 0
        visited = set()
        aux = self.n.copy()
        key = aux.pop()

        for i in self.n:
            if i not in visited:
                visited.add(i)

                if graph._data[i].connect == []:
                    count += 1

                    
                else:
                    count += 1
                    for adj in graph._data[i].connect:
                        visited.add(i)


    def convertToBFSTree(self, graph, v):

        if self.isConnected() == False: raise Exception("graph is not connected")

        key = v

        visited = set()
        edges = []
        queue =[(key, None)]

        while queue:
            ## Aux va a ser el nodo de referencia "head"
            node, parent = queue.pop(0) 

            if node not in visited: 
                visited.add(node)

                if parent is not None:
                    edges.append((parent, node))

                
                ## Se recorre los vertices adacentes del node
                for adj in graph._data[node].connect:
                    if adj not in visited:
                        queue.append((adj, node))
        
        new_graph = Graph(self.n)
        new_graph.createGraph(self.n, edges)

        return new_graph
    
    def convertToDFSTree(self, graph, v):

        new_graph = Graph(graph.n)

        visited = set()
        edges = []
        node = graph._data[v]

        self.ConvertToDFS_recursive(graph, node, visited, edges)
        
        new_graph.createGraph(graph.n, edges)
        return new_graph

    def ConvertToDFS_recursive(self, graph, node, visited, edges):
            

        if node.key not in visited:

            visited.add(node.key)

            for adj in node.connect:

                if adj not in visited:

                    
                    edges.append((node.key, adj))
                    aux_node = graph._data[adj]

                    self.ConvertToDFS_recursive(graph, aux_node, visited, edges)
                    

    def bestRoad(self , graph ,  v1 , v2):

        bfs_tree = self.convertToBFSTree(graph, v1)
        visited = set()
        queue = [(v1, None)]

        while queue:
            node, prev = queue.pop(0)

            if node == v2:
                #Construyo la ruta desde v1 a v2
                path = []
                while prev is not None:
                    path.append((prev, node))
                    node, prev = prev, bfs_tree._data[prev].parent
                path.reverse()
                return path

            if node not in visited:
                visited.add(node)
                #El nodo anterior es el padre del nodo actual
                bfs_tree._data[node].parent = prev 
                #Recorro los nodos adyacentes
                for adj in bfs_tree._data[node].connect:
                    #Si el adyacente no ha sido visitado lo agrego a la cola
                    if adj not in visited:
                        queue.append((adj, node))

        return None
                
                
           

        

            
        













                    
                

            

        



        

        

        

        
        
        




