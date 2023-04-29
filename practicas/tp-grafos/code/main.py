import graph as g

# Initial Node and adjacency list
vertex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
adjacency_list = [(1, 2), (1, 4), (2, 3), (5, 1), (7, 8), (5, 7), (0, 3), (8, 6)]

# Initialize graph
graph = g.Graph(vertex_list)
graph.createGraph(vertex_list, adjacency_list)

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
graph.printGraph()

print( "-"*20, " ExistPath ", "-"*20)
# Case 1: Direct Link
print(graph.existPath(5, 7))

print( "-"*20, " IsConnected ", "-"*20)
print(graph.isConnected())

print( "-"*20, " IsTree ", "-"*20)
print(graph.isTree())







