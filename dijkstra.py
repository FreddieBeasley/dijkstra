from graph import *

class DijkstraVertex(Vertex):
     def __init__(self, label, order, cost, path=None):
          super().__init__(label)
          self.__order = order
          self.__cost = cost
          self.__path = path

     def get_order(self):
          return self.__order
     
     def get_cost(self):
          return self.__cost
     
     def get_path(self):
          return self.__path
     
     def update_order(self, order):
          self.__order = order
     
     def update_cost(self, cost):
          self.__cost = cost
     
     def update_path(self, label):
          self.__path = label

class Queue:
     def __init__(self):
          self.__discovered = []
          self.__resolved = []

     def add(self, dijkstraVertex):
          self.__discovered.append(dijkstraVertex)

     def add_resolved(self, dijkstraVertex):
          self.__resolved.append(dijkstraVertex)

     def remove(self, dijkstraVertex):
          self.__discovered.remove(dijkstraVertex)
     
     def pop(self): #returns the dijkstraVertex with the lowest cost
          lowest = 100
          returnItem = None

          for dijkstraVertex in self.__discovered:
               if dijkstraVertex.get_cost() < lowest:
                    lowest = dijkstraVertex.get_cost()
                    returnItem = dijkstraVertex
          
          self.__resolved.append(returnItem)
          self.__discovered.remove(returnItem)
          return returnItem
     
     def lookUp_dijkstraVertex(self, label):
          for dijkstraVertex in self.__discovered:
               if dijkstraVertex.get_label() == label:
                    return dijkstraVertex
          return None
     
     def lookUp_dijkstraVertex_resolved(self, label):
          for dijkstraVertex in self.__resolved:
               if dijkstraVertex.get_label() == label:
                    return dijkstraVertex
          return None
     
     def get_discovered(self):
          return self.__discovered
     
     def get_resolved(self):
          return self.__resolved
     
     def __len__(self):
          return len(self.__discovered)


#returns the shortest paths to all vertices
def dijkstra(graph:Graph, startVertex:Vertex, endVertex:Vertex = None) -> list:

     #Checking is an endVertex has been entered
     specific = False
     if endVertex != None:
          specific = True

     #validation
     if startVertex not in graph.get_vertices():
          return []
     
     if endVertex not in graph.get_vertices() and specific:
          return []

     #initialising queue
     queue = Queue()
     queue.add(DijkstraVertex(
          label=startVertex.get_label(),
          order=None,
          cost=0,
          path=startVertex.get_label()
     ))

     order = -1

     while True:
          order += 1
          #Base case - all vertices resolved
          if len(queue) == 0:
               break

          currentDijkstraVertex = queue.pop()
          currentDijkstraVertex.update_order(order)

          #Base base - specific vertex is next to resolve
          if specific:
               if currentDijkstraVertex.get_label() == endVertex.get_label():
                    break

          for vertex_label, path_weight in graph.get_adjacency_list()[currentDijkstraVertex.get_label()]:

               if queue.lookUp_dijkstraVertex_resolved(vertex_label) is not None:
                    continue
               
               elif queue.lookUp_dijkstraVertex(vertex_label) is not None:
                    consideringDijkstraVertex = queue.lookUp_dijkstraVertex(vertex_label)

                    new_cost = currentDijkstraVertex.get_cost() + path_weight
                    old_cost = consideringDijkstraVertex.get_cost()

                    if old_cost > new_cost:
                         consideringDijkstraVertex.update_cost(new_cost)
                         consideringDijkstraVertex.update_path(currentDijkstraVertex.get_path() + consideringDijkstraVertex.get_label())

               else:
                    discoveredDijkstraVertex = DijkstraVertex(
                         label=vertex_label,
                         order=None,
                         cost=currentDijkstraVertex.get_cost() + path_weight
                    )

                    queue.add(discoveredDijkstraVertex)
                    discoveredDijkstraVertex.update_path(currentDijkstraVertex.get_path() + discoveredDijkstraVertex.get_label())
               
     if specific:
          if queue.lookUp_dijkstraVertex_resolved(endVertex.get_label()) == None: #end vertex has not been found
               return []
          
          endVertexDijkstra = queue.lookUp_dijkstraVertex_resolved(endVertex.get_label())
          return [f"vertex: {endVertexDijkstra.get_label()}", f"order: {endVertexDijkstra.get_order()}", f"cost: {endVertexDijkstra.get_cost()}", f"path: {endVertexDijkstra.get_path()}"]
     
     return [[f"vertex: {item.get_label()}", f"order: {item.get_order()}", f"cost: {item.get_cost()}", f"path: {item.get_path()}"] for item in queue.get_resolved()]

def test_dijkstra():
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

     # --- Test 1: my_graph ---
     print("\n--- Test 1: my_graph ---")
     print(dijkstra(my_graph, vertexA, vertexC))
     print("\n")
     print(dijkstra(my_graph, vertexA))
     print("\n")
     print(dijkstra(my_graph, vertexB))

     # --- Test 2: circular_graph ---
     print("\n--- Test 2: circular_graph ---")
     print(dijkstra(circular_graph, vertexA, vertexE))
     print("\n")
     print(dijkstra(circular_graph, vertexC))
     print("\n")
     print(dijkstra(circular_graph, vertexF))

     # --- Test 3: linear_graph ---
     print("\n--- Test 3: linear_graph ---")
     print(dijkstra(linear_graph, vertexA, vertexG))
     print("\n")
     print(dijkstra(linear_graph, vertexD))
     print("\n")
     print(dijkstra(linear_graph, vertexB))

     # --- Test 4: tree_graph ---
     print("\n--- Test 4: tree_graph ---")
     print(dijkstra(tree_graph, vertexA, vertexE))
     print("\n")
     print(dijkstra(tree_graph, vertexB))
     print("\n")
     print(dijkstra(tree_graph, vertexC))

     # --- Test 5: disconnected_graph ---
     print("\n--- Test 5: disconnected_graph ---")
     print(dijkstra(disconnected_graph, vertexA, vertexF))
     print("\n")
     print(dijkstra(disconnected_graph, vertexA))
     print("\n")
     print(dijkstra(disconnected_graph, vertexH))

test_dijkstra()