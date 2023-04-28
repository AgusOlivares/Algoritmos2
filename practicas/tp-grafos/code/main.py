import graph as g

# Initial Node and adjacency list
vertex_list = [1, 2, 3, 4]
adjacency_list = [(1, 2), (1, 4), (2, 3)]

# Initialize graph
graph = g.Graph(vertex_list)
graph.createGraph(vertex_list, adjacency_list)

# Insert new Node
graph.insert(0)

# Insert existing Node
#graph.insert(1)

# Create new Link
graph.link(0, 1)

# Try Existing link
#graph.link(2, 1)

graph.printGraph()