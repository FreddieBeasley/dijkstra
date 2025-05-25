class Vertex:
     def __init__(self, label):
          self.__label = label
     
     def get_label(self):
          return self.__label

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
          self.__adjacency_list[vertex.get_label()] = []
     
     def add_edge(self, edge:Edge):
          #validate edge
          for vertex in edge.get_vertices():
               if vertex not in self.__vertices:
                    return

          self.__edges.append(edge)

          #update adjacency list
          vertexA, vertexB = edge.get_vertices()

          self.__adjacency_list[vertexA.get_label()].append((vertexB.get_label(),edge.get_weight()))

          self.__adjacency_list[vertexB.get_label()].append((vertexA.get_label(),edge.get_weight()))
          
     def lookUp_vertex(self, label:str):
          for vertex in self.__vertices:
               if vertex.get_label() == label:
                    return vertex
          return None