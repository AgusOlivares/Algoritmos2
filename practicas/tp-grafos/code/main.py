import graph as g


 # Initial Node and adjacency list
vertex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
adjacency_list = [(1, 2), (1, 4), (2, 3), (5, 1), (7, 8), (5, 7), (0, 3), (8, 6)]


 # Initialize graph
graph = g.Graph(vertex_list)
graph.createGraph(vertex_list, adjacency_list)

vert = [1, 2, 3, 4]; adj = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (4, 3)]
graph1 = g.Graph(vert)
graph1.createGraph(vert, adj)

vertex = [1, 2, 3, 4, 5, 6, 7]; adjacency = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 5)]
graph2 = g.Graph(vertex); graph2.createGraph(vertex, adjacency)
 # Insert new Node
 #graph.insert(0)  
 #graph.insert(7)


 # Insert existing Node
 #graph.insert(1)

 # Create new Link
 #graph.link(0, 3) 

 # Try Existing link
 #graph.link(2, 1)

 # Create link of nonexisting node
 #graph.link(13, 2)

print( "-"*20, " Graph ", "-"*20)
print(graph.n)
 #graph.printGraph()

graph.printGraph()

print( "-"*20, " ExistPath ", "-"*20)
# Case 1: Direct Link
#print(graph.existPath(5, 7))
#print(graph1.existPath(1, 3))


print( "-"*20, " IsConnected ", "-"*20)
print(graph1.isConnected())

print( "-"*20, " IsTree ", "-"*20)
print(graph1.isTree(graph1))

print( "-"*20, " IsComplete ", "-"*20)
print(graph.isComplete())

print( "-"*20, " convertTree ", "-"*20)
print(graph.convertTree)

print( "-"*20, " ConvertToBFSTree ", "-"*20)
graph2.convertToBFSTree(graph2, 1).printGraph()

print( "-"*20, " ConvertToDFS ", "-"*20)
graph2.convertToDFSTree(graph2, 1).printGraph()

print( "-"*20, " BestRoadTo ", "-"*20)
print(graph.bestRoad(graph, 1, 15))

vert = [1, 2, 3, 4]; adj = [(1, 2, 4), (1, 3, 1), (1, 4, 6)]
graph1 = g.Graph(vert)
graph1.createPonderedGraph(vert, adj)
print("jjj")








