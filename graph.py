class Vertex:
     def __init__(self, lable):
          self.__lable = lable
     
     def get_lable(self):
          return self.__lable

class Edge:
     def __init__(self, weight, vertexA:Vertex, vertexB:Vertex):
          self.__weight = weight
          self.__vertexA = vertexA
          self.__vertexB = vertexB

     def get_weight(self):
          return self.__weight
     
     def get_vertices(self):
          return [self.__vertexA, self.__vertexB]
     
class Graph:
     def __init__(self):
          self.__vertices = []
          self.__edges = []

          self.__adjacency_list = {}

     #Getter
     def get_vertices(self):
          return self.__vertices
     
     def get_edges(self):
          return self.__edges
     
     def get_adjacency_list(self):
          return self.__adjacency_list
     
     #Adder
     def add_vertex(self, vertex:Vertex):
          self.__vertices.append(vertex)

          #update adjacency list
          self.__adjacency_list[vertex.get_lable()] = []
     
     def add_edge(self, edge:Edge):
          #validate edge
          for vertex in edge.get_vertices():
               if vertex not in self.__vertices:
                    return

          self.__edges.append(edge)

          #update adjacency list
          vertexA, vertexB = edge.get_vertices()

          self.__adjacency_list[vertexA.get_lable()].append((vertexB.get_lable(),edge.get_weight()))

          self.__adjacency_list[vertexB.get_lable()].append((vertexA.get_lable(),edge.get_weight()))
          
     def lookUp_vertex(self, lable:str):
          for vertex in self.__vertices:
               if vertex.get_lable() == lable:
                    return vertex
          return None

#----graphs-for-testing----

#vertices
vertexA = Vertex("a")
vertexB = Vertex("b")
vertexC = Vertex("c")
vertexD = Vertex("d")
vertexE = Vertex("e")
vertexF = Vertex("f")
vertexG = Vertex("g")
vertexH = Vertex("h")

#graph1 - original graph
my_graph = Graph()

my_graph.add_vertex(vertexA)
my_graph.add_vertex(vertexB)
my_graph.add_vertex(vertexC)
my_graph.add_vertex(vertexD)
my_graph.add_vertex(vertexE)

my_graph.add_edge(Edge(5,vertexA, vertexB))
my_graph.add_edge(Edge(7,vertexA, vertexC))
my_graph.add_edge(Edge(8,vertexB, vertexC))
my_graph.add_edge(Edge(4,vertexB, vertexD))
my_graph.add_edge(Edge(4,vertexC, vertexD))
my_graph.add_edge(Edge(6,vertexC, vertexE))
my_graph.add_edge(Edge(5,vertexD, vertexE))

#graph2 - circular graph
circular_graph = Graph()

circular_graph.add_vertex(vertexA)
circular_graph.add_vertex(vertexB)
circular_graph.add_vertex(vertexC)
circular_graph.add_vertex(vertexD)
circular_graph.add_vertex(vertexE)
circular_graph.add_vertex(vertexF)

circular_graph.add_edge(Edge(3,vertexA,vertexB))
circular_graph.add_edge(Edge(3,vertexB,vertexC))
circular_graph.add_edge(Edge(3,vertexC,vertexD))
circular_graph.add_edge(Edge(3,vertexD,vertexE))
circular_graph.add_edge(Edge(3,vertexE,vertexF))
circular_graph.add_edge(Edge(3,vertexF,vertexA))

#graph3 - linear graph
linear_graph = Graph()

linear_graph.add_vertex(vertexA)
linear_graph.add_vertex(vertexB)
linear_graph.add_vertex(vertexC)
linear_graph.add_vertex(vertexD)
linear_graph.add_vertex(vertexE)
linear_graph.add_vertex(vertexF)

linear_graph.add_edge(Edge(3,vertexA,vertexB))
linear_graph.add_edge(Edge(1,vertexB,vertexC))
linear_graph.add_edge(Edge(4,vertexC,vertexD))
linear_graph.add_edge(Edge(1,vertexD,vertexE))
linear_graph.add_edge(Edge(5,vertexE,vertexF))

#graph4 - tree graph
tree_graph = Graph()

tree_graph.add_vertex(vertexA)
tree_graph.add_vertex(vertexB)
tree_graph.add_vertex(vertexC)
tree_graph.add_vertex(vertexD)
tree_graph.add_vertex(vertexE)
tree_graph.add_vertex(vertexF)
tree_graph.add_vertex(vertexG)
tree_graph.add_vertex(vertexH)

tree_graph.add_edge(Edge(4,vertexA,vertexB))
tree_graph.add_edge(Edge(7,vertexB,vertexD))
tree_graph.add_edge(Edge(1,vertexD,vertexE))
tree_graph.add_edge(Edge(9,vertexB,vertexC))
tree_graph.add_edge(Edge(2,vertexA,vertexF))
tree_graph.add_edge(Edge(1,vertexF,vertexH))
tree_graph.add_edge(Edge(3,vertexF,vertexG))

#graph5 - disconnected graph
disconnected_graph = Graph()

disconnected_graph.add_vertex(vertexA)
disconnected_graph.add_vertex(vertexB)
disconnected_graph.add_vertex(vertexC)
disconnected_graph.add_vertex(vertexD)
disconnected_graph.add_vertex(vertexE)
disconnected_graph.add_vertex(vertexF)
disconnected_graph.add_vertex(vertexG)

disconnected_graph.add_edge(Edge(4,vertexA,vertexB))
disconnected_graph.add_edge(Edge(3,vertexB,vertexC))
disconnected_graph.add_edge(Edge(2,vertexC,vertexA))
disconnected_graph.add_edge(Edge(1,vertexD,vertexE))
disconnected_graph.add_edge(Edge(4,vertexE,vertexF))



