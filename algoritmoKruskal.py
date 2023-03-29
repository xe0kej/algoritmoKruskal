"""
Algoritmo de Kruskal

Estudiantes:
Jesus Perez - C.I: 27.877.780
Alexander Castillo - C.I: 28.517.461

Asignatura: Estructuras Discretas II
"""

from operator import itemgetter

class Kruskal:

    def __init__(self):
        self.nodes=[]
        self.order=[]
        self.nodes = {}
        self.order = {}

    def prepare_data(self, node):
        self.nodes[node] = node
        self.order[node] = 0

    def find_node(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_node(self.nodes[node])
        return self.nodes[node]

    def validate_union(self, origin, destination):
        origin_auxiliar = self.find_node(origin)
        destination_auxiliar = self.find_node(destination)
        if origin_auxiliar != destination_auxiliar:
            if self.order[origin_auxiliar] > self.order[destination_auxiliar]:
                self.nodes[destination_auxiliar] = origin_auxiliar
            else:
                self.nodes[origin_auxiliar] = destination_auxiliar
                if self.order[origin_auxiliar] == self.order[destination_auxiliar]:
                    self.order[destination_auxiliar] += 1

    def kruskal(self, nodes, edges):
        tree = []
        for node in nodes: 
            self.prepare_data(node)
        edges.sort(key = itemgetter(2))
        for edge in edges:
            origin, destination, weight = edge
            if self.find_node(origin) != self.find_node(destination):
                self.validate_union(origin, destination)
                tree.append(edge)
        return tree

obj_kruskal = Kruskal()

nodes = ['1','2','3','4','5','6','7','8','9']

edges = [['1','2',4],['1','3',9],['2','5',9],['2','3',11],['3','4',7],['3','6',1],['4','6',6],['5','4',2],['5','8',4],['6','8',2],
['7','5',7],['7','9',10],['8','7',15],['8','9',11]]

tree = obj_kruskal.kruskal(nodes, edges)
print("El arbol obtenido es: ")
print(tree)
print("")
path = 0
for edge in tree:
    path += edge[2]
print("El peso del arbol es: " + str(path))
