import graph as g

lista_vertices = [1, 2, 3, 4]

lista_adyacencia = [(1, 2), (1, 4), (2, 3)]

grafo = g.Graph(lista_vertices)
grafo.createGraph(lista_vertices, lista_adyacencia)

grafo.insert(0)

grafo.link(0, 1)

print(grafo._data.fromkeys)