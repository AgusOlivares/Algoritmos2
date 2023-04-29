
class GraphNode:

    def __init__(self, key = None, color = "white") -> None:
        self.key = key 
        self.color = color
        self.connect = [] # funcionaria agregar un set() y en vez de append() un add()?

class Graph:

    def __init__(self, n) -> None: 
        
        ## nodes in graph
        self.n = n    

        ## Test, data is stored in dictionary
        self._data : dict[list[GraphNode]] = {}

        
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

    def existPath(self, graph, v0, v1):

        if v0 not in graph._data or v1 not in graph._data:
            raise Exception("One or both vs not in graph")
        
        if v0 == v1: return True
        
        for i in graph._data[v0].connect:
            if v1 in graph._data[v0].connect:
                return True
            else:
                return self.existPath(graph , i , v1)

        return False
    
    def isConnected(self, graph):  ## RESOLVER Error

        been = set([])

        key = 0

        lista = Graph.isConnected_recursive(graph, been, key)

        return lista == graph.n
        

       

    def isConnected_recursive(graph, been, key):

        node = graph._data[key]
        
        for i in node.connect:
            
            if i in been:
                continue
            else:
                been.add(i)

            graph.isConnected_recursive(graph , been , i)
        
        return been

    


                    
                

            

        



        

        

        

        
        
        




