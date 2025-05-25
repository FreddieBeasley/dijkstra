from graph import *

#Not used in the end
"""
def getAdjacentVertices(graph:Graph, vertex:Vertex) -> list:
     returnlist = []

     for edge in graph.get_edges():
          
          if vertex == edge.get_vertices()[0] and edge.get_vertices()[1] not in returnlist:
               returnlist.append(edge.get_vertices()[1])

          elif vertex == edge.get_vertices()[1] and edge.get_vertices()[0] not in returnlist:
               returnlist.append(edge.get_vertices()[0])
     
     return returnlist
"""

class DijkstraVertex(Vertex):
     def __init__(self, lable, order, count, path=None):
          super().__init__(lable)
          self.__order = order
          self.__count = count
          self.__path = path
     
     def get_order(self):
          return self.__order
     
     def get_count(self):
          return self.__count
     
     def get_path(self):
          return self.__path
     
     def get_path_reverse(self):
          #logic means that path is stored in reverse
          return self.__path

     
     def update_order(self, order):
          self.__order = order
     
     def update_count(self, count):
          self.__count = count
     
     def update_path(self, lable):
          self.__path = lable

class Queue:
     def __init__(self):
          self.__discovered = []
          self.__resolved = []

     def add(self, dijkstraVertex):
          self.__discovered.append(dijkstraVertex)
     
     def pop(self): #returns the DikstraItem with the lowest count
          lowest = 100
          returnItem = None

          for dijkstraVertex in self.__discovered:
               if dijkstraVertex.get_count() < lowest:
                    lowest = dijkstraVertex.get_count()
                    returnItem = dijkstraVertex
          
          self.__resolved.append(returnItem)
          self.__discovered.remove(returnItem)
          return returnItem
     
     def lookUp_dijkstraVertex(self, lable):
          for dijkstraVertex in self.__discovered:
               if dijkstraVertex.get_lable() == lable:
                    return dijkstraVertex
          return None
     
     def lookUp_dijkstraVertex_resolved(self, lable):
          for dijkstraVertex in self.__resolved:
               if dijkstraVertex.get_lable() == lable:
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
          lable=startVertex.get_lable(),
          order=None,
          count=0,
          path=startVertex.get_lable()
     ))

     order = -1

     while True:
          order += 1
          #Base case - all vertices resolved
          if len(queue) == 0:
               break

          currentDijkstraItem = queue.pop()
          currentDijkstraItem.update_order(order)

          #Base base - specific vertex is next to resolve
          if specific:
               if currentDijkstraItem.get_lable() == endVertex.get_lable():
                    break

          for vertex_lable, path_weight in graph.get_adjacency_list()[currentDijkstraItem.get_lable()]:
               
               if queue.lookUp_dijkstraVertex_resolved(vertex_lable) is not None:
                    continue
               
               elif queue.lookUp_dijkstraVertex(vertex_lable) is not None:
                    consideringDijkstraVertex = queue.lookUp_dijkstraVertex(vertex_lable)

                    new_count = currentDijkstraItem.get_count() + path_weight
                    old_count = consideringDijkstraVertex.get_count()

                    if old_count > new_count:
                         consideringDijkstraVertex.update_count(new_count)
                         consideringDijkstraVertex.update_path(currentDijkstraItem.get_path() + consideringDijkstraVertex.get_lable())

               else:
                    discoveredDijkstraVertex = DijkstraVertex(
                         lable=vertex_lable,
                         order=None,
                         count=currentDijkstraItem.get_count() + path_weight
                    )

                    queue.add(discoveredDijkstraVertex)
                    discoveredDijkstraVertex.update_path(currentDijkstraItem.get_path() + discoveredDijkstraVertex.get_lable())
               
          '''
          for edge in graph.get_edges():
               #loops through each vertex in the graph

               if edge.get_vertices()[0] == graph.lookUp_vertex(currentDijkstraItem.get_lable()):
                    #selects vertices which are adjacent to current vertex
                    consideringDijkstraItem = queue.lookUp_item(edge.get_vertices()[1].get_lable())

               elif edge.get_vertices()[1] == graph.lookUp_vertex(currentDijkstraItem.get_lable()):
                    consideringDijkstraItem = queue.lookUp_item(edge.get_vertices()[0].get_lable())

               else:
                    continue

               if consideringDijkstraItem == None:
                    continue
               
               currentRouteCost = consideringDijkstraItem.get_count()
               newRouteCost = currentDijkstraItem.get_count() + edge.get_weight()

               if currentRouteCost > newRouteCost:
                    consideringDijkstraItem.update_count(newRouteCost)
                    consideringDijkstraItem.update_path(currentDijkstraItem.get_path())
               '''
     if specific:
          endVertexDijkstra = queue.lookUp_dijkstraVertex_resolved(endVertex.get_lable())
          return [f"vertex: {endVertexDijkstra.get_lable()}", f"order: {endVertexDijkstra.get_order()}", f"cost: {endVertexDijkstra.get_count()}", f"path: {endVertexDijkstra.get_path_reverse()}"]
     
     return [[f"vertex: {item.get_lable()}", f"order: {item.get_order()}", f"cost: {item.get_count()}", f"path: {item.get_path_reverse()}"] for item in queue.get_resolved()]

'''
if you pass in a vertex that it not in the graph as the end vertex (e.g. linear graph test 1 where there is no vertex g), due to the lookUp_vertex returning None when the vertex cannot be found, None is passed in as the endVertex and therefore the dijkstra algorithm will just find the shortest path to all other nodes.
'''

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
print(dijkstra(disconnected_graph, vertexA, vertexH))
print("\n")
print(dijkstra(disconnected_graph, vertexA))
print("\n")
print(dijkstra(disconnected_graph, vertexH))