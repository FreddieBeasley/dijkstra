from dijkstra import *

class AstarVertex(Vertex):
     def __init__(self, label, heuristic=None):
          Vertex.__init__(self,label)

          self.__heuristic = heuristic
     
     def get_heuristic(self):
          return self.__heuristic
     
     def set_heuristic(self, value:int):
          self.__heuristic = value
     
class AstarGraph(Graph):
     def __init__(self):
          super().__init__()
     
     def add_vertex(self, vertex:AstarVertex, heuristic:int):
          super().add_vertex(vertex)

          vertex.set_heuristic(heuristic)

"""
class AstarGraph(Graph):
     def __init__(self):
          super().__init__()

          self.__heuristic_list = {}

     def get_heuristic_list(self):
          return self.__heuristic_list
     
     def add_vertex(self, vertex:AstarVertex, heuristic:int):
          super().add_vertex(vertex)

          vertex.set_heuristic(heuristic)
          self.__heuristic_list[vertex.get_label()] = heuristic
"""

#combination of AsterVertex and DijkstraVertex therefore has cost, path but also heuristic
class AstarDijkstraVertex(AstarVertex, DijkstraVertex):
     def __init__(self, label, order, cost, heuristic, path=None):
          AstarVertex.__init__(self,label, heuristic)
          DijkstraVertex.__init__(self, label, order, cost, path)

class AstarQueue(Queue):
     def __init__(self):
          super().__init__()

     def pop(self): #returns astarVertex with the lowest working value
          lowest = 1000
          
          for astarDijkstraVertex in self.get_discovered():
               currentCost = astarDijkstraVertex.get_cost()
               heuristicValue = astarDijkstraVertex.get_heuristic()

               workingValue = currentCost + heuristicValue

               if workingValue < lowest:
                    lowest = workingValue
                    returnItem = astarDijkstraVertex
          
          self.add_resolved(returnItem)
          self.remove(returnItem)
          return returnItem
     
def astar(graph:AstarGraph, startVertex:AstarVertex, endVertex:AstarVertex) -> list:

     #Validation
     if startVertex not in graph.get_vertices():
          return []
     
     if endVertex not in graph.get_vertices():
          return []
     
     #initialising queue
     queue = AstarQueue()
     queue.add(AstarDijkstraVertex(
          label=startVertex.get_label(),
          order=None,
          cost=0,
          heuristic=startVertex.get_heuristic(),
          path=startVertex.get_label()
     ))

     order = -1

     while True:
          order += 1

          #Base case - all discovered vertices resolved
          if len(queue) == 0:
               break

          currentAstarVertex = queue.pop()
          currentAstarVertex.update_order(order)

          #Base case - specific vertex is next to resolve
          if currentAstarVertex.get_label() == endVertex.get_label():
               break
          
          for vertex_label, path_weight in graph.get_adjacency_list()[currentAstarVertex.get_label()]:

               if queue.lookUp_dijkstraVertex_resolved(vertex_label) is not None:
                    continue

               elif queue.lookUp_dijkstraVertex(vertex_label) is not None:
                    consideringAstarVertex = queue.lookUp_dijkstraVertex(vertex_label)

                    new_cost = currentAstarVertex.get_cost() + path_weight
                    old_cost = consideringAstarVertex.get_cost()

                    if old_cost > new_cost:
                         consideringAstarVertex.update_cost(new_cost)
                         consideringAstarVertex.update_path(currentAstarVertex.get_path() + consideringAstarVertex.get_label())

               else:
                    discoveredAstarVertex = AstarDijkstraVertex(
                         label=vertex_label,
                         order=None,
                         cost=currentAstarVertex.get_cost() + path_weight,
                         heuristic= graph.lookUp_vertex(vertex_label).get_heuristic()
                    )

                    queue.add(discoveredAstarVertex)
                    discoveredAstarVertex.update_path(currentAstarVertex.get_path() + discoveredAstarVertex.get_label())
               

     if queue.lookUp_dijkstraVertex_resolved(endVertex.get_label()) == None:
          return []
     
     endVertexAstar = queue.lookUp_dijkstraVertex_resolved(endVertex.get_label())

     return [f"vertex: {endVertexAstar.get_label()}", f"order: {endVertexAstar.get_order()}", f"cost: {endVertexAstar.get_cost()}", f"path: {endVertexAstar.get_path()}"]


def test_astar():
     #----graphs-for-testing----

     #vertices
     vertexA = AstarVertex("a")
     vertexB = AstarVertex("b")
     vertexC = AstarVertex("c")
     vertexD = AstarVertex("d")
     vertexE = AstarVertex("e")
     vertexF = AstarVertex("f")
     vertexG = AstarVertex("g")
     vertexH = AstarVertex("h")

     #graph1 - original graph
     my_graph = AstarGraph()

     my_graph.add_vertex(vertexA,0)
     my_graph.add_vertex(vertexB,4)
     my_graph.add_vertex(vertexC,5)
     my_graph.add_vertex(vertexD,8)
     my_graph.add_vertex(vertexE,9)

     my_graph.add_edge(Edge(5,vertexA, vertexB))
     my_graph.add_edge(Edge(7,vertexA, vertexC))
     my_graph.add_edge(Edge(8,vertexB, vertexC))
     my_graph.add_edge(Edge(4,vertexB, vertexD))
     my_graph.add_edge(Edge(4,vertexC, vertexD))
     my_graph.add_edge(Edge(6,vertexC, vertexE))
     my_graph.add_edge(Edge(5,vertexD, vertexE))

     #graph2 - circular graph
     circular_graph = AstarGraph()

     circular_graph.add_vertex(vertexA,0)
     circular_graph.add_vertex(vertexB,3)
     circular_graph.add_vertex(vertexC,6)
     circular_graph.add_vertex(vertexD,9)
     circular_graph.add_vertex(vertexE,7)
     circular_graph.add_vertex(vertexF,3)

     circular_graph.add_edge(Edge(3,vertexA,vertexB))
     circular_graph.add_edge(Edge(3,vertexB,vertexC))
     circular_graph.add_edge(Edge(3,vertexC,vertexD))
     circular_graph.add_edge(Edge(3,vertexD,vertexE))
     circular_graph.add_edge(Edge(3,vertexE,vertexF))
     circular_graph.add_edge(Edge(3,vertexF,vertexA))

     #graph3 - linear graph
     linear_graph = AstarGraph()

     linear_graph.add_vertex(vertexA,0)
     linear_graph.add_vertex(vertexB,2)
     linear_graph.add_vertex(vertexC,3)
     linear_graph.add_vertex(vertexD,7)
     linear_graph.add_vertex(vertexE,8)
     linear_graph.add_vertex(vertexF,12)

     linear_graph.add_edge(Edge(3,vertexA,vertexB))
     linear_graph.add_edge(Edge(1,vertexB,vertexC))
     linear_graph.add_edge(Edge(4,vertexC,vertexD))
     linear_graph.add_edge(Edge(1,vertexD,vertexE))
     linear_graph.add_edge(Edge(5,vertexE,vertexF))

     #graph4 - tree graph
     tree_graph = AstarGraph()

     tree_graph.add_vertex(vertexA,0)
     tree_graph.add_vertex(vertexB,3)
     tree_graph.add_vertex(vertexC,10)
     tree_graph.add_vertex(vertexD,10)
     tree_graph.add_vertex(vertexE,11)
     tree_graph.add_vertex(vertexF,2)
     tree_graph.add_vertex(vertexG,4)
     tree_graph.add_vertex(vertexH,3)

     tree_graph.add_edge(Edge(4,vertexA,vertexB))
     tree_graph.add_edge(Edge(7,vertexB,vertexD))
     tree_graph.add_edge(Edge(1,vertexD,vertexE))
     tree_graph.add_edge(Edge(9,vertexB,vertexC))
     tree_graph.add_edge(Edge(2,vertexA,vertexF))
     tree_graph.add_edge(Edge(1,vertexF,vertexH))
     tree_graph.add_edge(Edge(3,vertexF,vertexG))

     #graph5 - disconnected graph
     disconnected_graph = AstarGraph()

     disconnected_graph.add_vertex(vertexA,0)
     disconnected_graph.add_vertex(vertexB,3)
     disconnected_graph.add_vertex(vertexC,2)
     disconnected_graph.add_vertex(vertexD,6)
     disconnected_graph.add_vertex(vertexE,7)
     disconnected_graph.add_vertex(vertexF,9)
     disconnected_graph.add_vertex(vertexG,8)

     disconnected_graph.add_edge(Edge(4,vertexA,vertexB))
     disconnected_graph.add_edge(Edge(3,vertexB,vertexC))
     disconnected_graph.add_edge(Edge(2,vertexC,vertexA))
     disconnected_graph.add_edge(Edge(1,vertexD,vertexE))
     disconnected_graph.add_edge(Edge(4,vertexE,vertexF))

     # --- Test 1: my_graph ---
     print("\n--- Test 1: my_graph ---")
     print(astar(my_graph, vertexE, vertexA))
     print("\n")
     print(astar(my_graph, vertexC, vertexA))
     print("\n")
     print(astar(my_graph, vertexD, vertexA))

test_astar()