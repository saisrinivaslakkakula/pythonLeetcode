'''
Dijkstra's Algorithm:

Dijkstra's Algorithm is used to find shortest path between source node to any other node in the graph.
I's possible for only Directed Asyclic and Weighted graph.
This is usually done by making all the nodes's distance to infinity except the current node.
Traverse through all the nodes, check if the nodes/ it's one by one neighbors  are visited already or not:
 if not, calculate the  weight of next neighbor(s) by formula:
 Current weight at node + weight of edge to the neighbor node.

 If the neighbor node has weight which is greater than the resultant of the above calculation, that means the resultant
 we calculated is the shortest path compared to the path that has alreay been calculated to that neighbor node.
 We change the value of neighbor node's weight to calculated one.
 if resultant is greater we ignore.

 In any case we need to mark the current node as visited after successfully processing all the neighbors.

 Hence all the resultant distances are calculated in the end.

 While traversing the graph, once the visited node is marked as visited, unlike BFS or DFS, we don't have choice to select
 the next nodes to visit here.

 We need to calculate the minimum weight among the un visited nodes and take the best minimum for processing.

 Remember node's weight may change at any point in traversal but it is visited if and only of it processed with all the neighbors.

We keep track of unvisited nodes in a set by removing visted after the visit is complete.

We loop the remaining un visited nodes everytime over the set and find the minimum among the un visited nodes from the set.

Refer to Dijkshtra.png for more clarity

'''
from collections import defaultdict
class Graph:
    def __init__(self):
        '''
        This graph class is a bot different than we've seen before. this has nodes in seperate set
        edges connectin the nodes in seperate dict
        weights/ distances  of those edges in seperate dict
        Suppose A -----4-----B
        Edge connceting nodes A,B has weight 4, we insert this value in map like the one shown below
        weights[(A,B)] = 4
        '''
        self.nodes = set()
        self.edges = defaultdict()
        self.weights = {}

    def addNode(self,node):
        #Simply add node to the set
        self.nodes.add(node)

    def addEdge(self,fromNode,ToNode,dist):
        # add edge connecting (source,Dest) and it's weight as key value pair
        if fromNode in self.edges:
            self.edges[fromNode].append(ToNode)
            self.weights[(fromNode,ToNode)] = dist
        else:
            self.edges[fromNode] = [ToNode]
            self.weights[(fromNode, ToNode)] = dist

def dijkstra(graph,initNode):
    visited = dict() # keep track of already visited nodes
    visited[initNode]=0 # our sorce node is visited by default initially
    path = defaultdict(list) # keep track of paths
    nodes = set(graph.nodes) # take another copy of nodes so that we can remove visited nodes from the replicated set rather than the origional
    while nodes: # as long as set contains un visited nodes
        minnode = None # initiate min node to none
        for node in nodes: # check all the unvisited nodes and find the minimum among them. we need to process this node only.
            if node in visited:
                if minnode is None: # obviously first unvisited node will be the min node
                    minnode = node
                elif visited[node] < visited[minnode]: # if any node has lesser weight than above initiated node, that is minimum.
                    minnode = node
        if minnode is None: # if no node is found minimum, that means traveral is complete and break the loop.
            break
        nodes.remove(minnode) # as soon as min node is found, remove it from the set since it's visited.
        cur_weight = visited[minnode] # get the current weight of min node.
        if minnode in graph.edges:
            neighbors = graph.edges[minnode]
            for neighbor in neighbors: # traverse all unvisited neighbor nodes and check the resultant weight using the below formula
                #print(graph.weights)
                new_weight = cur_weight+graph.weights[(minnode,neighbor)]
                if neighbor not in visited or new_weight < visited[neighbor]:
                    visited[neighbor] = new_weight # if resultant is less than current weight of neighbor, replace it
                    path[minnode] = neighbor # add it to path minnode->neighbor as path

    return visited,path # finally, after breaking the loop return the weights and path.
    # weights give the shortest dist form node Source to node Destination and path gives it's respective path.



graph = Graph()
#for git op
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")
graph.addNode("F")
graph.addNode("G")

graph.addEdge("A","B",2)
graph.addEdge("A","C",5)
graph.addEdge("B","C",6)
graph.addEdge("B","D",1)
graph.addEdge("B","E",3)
graph.addEdge("C","F",8)
graph.addEdge("D","E",4)
graph.addEdge("E","G",9)
graph.addEdge("F","G",7)
print(graph.weights)

print(dijkstra(graph,"A"))

