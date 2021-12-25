'''
There are different types of graph
Main seggregation is wether graph is directed or un directed
second is if its' weighted otr unweighted
third is, if it's weighted, wether is is positive weighted or negative weighted

This gives us 6 types of graphs
directed weighted positive graph
directed weighted negative graph
directed unweigted graph
undirected weighted positive graph
undirected weighted negative graph
undirected unweighted graph

Also, The graph can be cyclic or uncyclic. uncyclic and directed graph is basically a tree data structure.

To construct  a graph, we use two data structures
1. 2D array or adjacency matrix
2. 1D array or adjacency list ==> Dictionary in case of python

To see how these representations look like , refer to Graph Representaions.png

in the fig. the adjacency matrix is constucted by n x n where n represents no. of vertices or nodes.
In the fig. there are 4 vertices in the graph. Whch means we need 4 X 4 Matrix.
[Graph is a directed one in the fig ]
    -> Construct 4x4 matrix with all 0's in it.
    -> start from any one of the vertices and check their respective connecting vertices. In other words check it's edges.
    -> for each vertex as row, and connected vertex as column, fill in the 1 if it's connected.

  suppose A is connected to B. Then the row is A and column is B. cell representing [A] [B] is set to 1.

In case of Adjacency list, we store the vertex as key and connceted edges as values in a python dictionary.

Now let's look at examples of adding edges to vertices.

'''
from collections import deque
class Graph:
    def __init__(self,graphDict = None):
        if graphDict is None:graphDict = {}
        self.graphDict = graphDict

    def addEdge(self,vertex,edge):
        if vertex in self.graphDict:
            self.graphDict[vertex].append(edge)
        else:
            self.graphDict[vertex] = [edge]

    def graphBFS(self,vertex):
        visited = set()
        queue = deque()
        visited.add(vertex)
        queue.append(vertex)
        while len(queue) >0:
            #print(queue)
            cur_vertex = queue.popleft()
            #print(self.graphDict)
            #print(cur_vertex)
            if cur_vertex in self.graphDict:
                edges = self.graphDict[cur_vertex]
                #print(edges)
            else: edges = []
            for edge in edges:
                if edge not in visited:
                    queue.append(edge)
                    visited.add(edge)

        print(visited)

    def graphDFS(self,vertex):
        stack =[vertex]
        visited = {vertex}
        while stack:
            curr_vertex = stack.pop()
            #print(curr_vertex)
            if curr_vertex not in visited: visited.add(curr_vertex)
            if curr_vertex in self.graphDict:
                edges = self.graphDict[curr_vertex]
            else: edges = []
            for edge in edges:
                if edge not in visited: stack.append(edge)

        print(visited)

    def findZeroIncomingEdges(self):
        hasIncoming =set()
        for vertex in self.graphDict:
            adj = self.graphDict[vertex]
            for a in adj:
                if a not in hasIncoming: hasIncoming.add(a)
        incomingonlyList = []
        for vertex in self.graphDict:
            if vertex not in hasIncoming:incomingonlyList.append(vertex)
        print(incomingonlyList)




    def printGraph(self):
        print(self.graphDict)

temp_graph = dict()

#temp_graph = {"A":["B","C","D"],"B":["D"],"C":["B"],"D":["C"]}

temp_graph = {}
customGraph = Graph(temp_graph)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")
customGraph.printGraph()
customGraph.findZeroIncomingEdges()
