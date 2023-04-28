
class GraphNode:

    def __init__(self, key = None, color = "white") -> None:
        self.key = key 
        self.color = color
        self.connect = []

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

        node0 = self._data[vertice0]
        node1 = self._data[vertice1]
        
        if vertice1 in node0.connect:
            raise Exception("Link already exist in graph")

        if vertice0 in node1.connect:
            raise Exception("Link already exist in graph")
        
        node0.connect.append(vertice1)
        node1.connect.append(vertice0)

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
