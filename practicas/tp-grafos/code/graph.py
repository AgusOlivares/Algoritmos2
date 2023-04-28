
class GraphNode:

    def __init__(self, key = None, color = "white") -> None:
        self.key = key 
        self.color = color
        self.connect = []

class Graph:

    def __init__(self, vertices) -> None: 
        
        ## Cantidad de nodos que estaran presentes en el grafico
        self.vertices = vertices      

        ## Prueba, especifico que los datos son almacenados en un diccionario
        self._data : dict[list[GraphNode]] = {}

        
    def createGraph(self, vertices, aristas):

        for vertex in vertices:
            self.insert(vertex)
            

        for (vertice0, vertice1) in aristas:
            self.link(vertice0, vertice1)
            
        return 
        
        
    def link(self, vertice0, vertice1):
        
        self._data[vertice0].connect.append(vertice1)
        self._data[vertice1].connect.append(vertice0)

    def insert(self, vertice): 

        if vertice in self._data:
            raise Exception("El nodo ya existe")
        
        if vertice not in self.vertices:
            self.vertices.append(vertice)
        
        node = GraphNode(vertice)

        # Inserto como key el valor del vertice y creo un graphnode en la key
        self._data[vertice] = node


