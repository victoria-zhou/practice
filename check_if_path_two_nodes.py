# program to check if there is exist a path between two vertices of a graph
 
from collections import defaultdict

class Graph:
    def __init__(self, vertices_num):
        self.vertices = vertices_num
        self.graph = defaultdict(list)

    def add_node(self, vertice, node):
        self.graph[vertice].append(node)

    def have_path(self, vert_a, vert_b):
        visited = [False]*(self.vertices) # know how to use this

        queue =[]

        queue.append(vert_a)

        visited[vert_a] = True

        while queue:
            to_visit = queue.pop()
            if to_visit == vert_b:
                return True

            else:
                for i in self.graph[to_visit]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True

        return False

g = Graph(4)
g.add_node(0, 1)
g.add_node(0, 2)
g.add_node(1, 2)
g.add_node(2, 0)
g.add_node(2, 3)
g.add_node(3, 3)

u =1; v = 3

assert g.have_path(1, 3) 
assert not g.have_path(3, 1) 
