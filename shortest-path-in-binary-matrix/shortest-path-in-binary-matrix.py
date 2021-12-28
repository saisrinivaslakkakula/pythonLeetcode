from collections import deque
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict()
        self.weights = {}
        
    def addNode(self,node):
        self.nodes.add(node)
        #pass
        
    def addEdge(self,fromNode,toNode,weight):
        if fromNode in self.edges:
            self.edges[fromNode].append(toNode)
            self.weights[(fromNode,toNode)]= weight
        else:
            self.edges[fromNode] = [toNode]
            self.weights[(fromNode,toNode)]= weight
            
    def buildGraph(self,grid):
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j] == 0:
                    self.addNode((i,j))
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j] == 0:
                    if j-1 >=0 and grid[i][j-1] ==0:
                        self.addEdge((i,j),(i,j-1),1)
                    if j+1 <len(grid) and grid[i][j+1] ==0:
                        self.addEdge((i,j),(i,j+1),1)
                    if i-1 >=0 and grid[i-1][j] ==0:
                        self.addEdge((i,j),(i-1,j),1)
                    if i+1 <len(grid) and grid[i+1][j] ==0:
                        self.addEdge((i,j),(i+1,j),1)
                    if i-1 >=0 and j-1 >=0 and grid[i-1][j-1] ==0:
                        self.addEdge((i,j),(i-1,j-1),1)
                    if i+1 <len(grid) and j+1 <len(grid[0]) and grid[i+1][j+1] ==0:
                        self.addEdge((i,j),(i+1,j+1),1)
                    if i+1<len(grid) and j-1 >=0 and grid[i+1][j-1] ==0:
                        self.addEdge((i,j),(i+1,j-1),1)
                    if i-1 >=0 and j+1<len(grid[0]) and grid[i-1][j+1] ==0:
                        self.addEdge((i,j),(i-1,j+1),1)
                        
        
            
        
class Solution:
    def enqueNeighbors(self,grid,queue,dt,row_idx,col_idx):
        i,j,d = dt
        d+=1
        if j-1 >=0 and grid[i][j-1] ==0:
            queue.append((i,j-1,d))
            grid[i][j-1] = d
        if j+1 <len(grid) and grid[i][j+1] ==0:
            queue.append((i,j+1,d))
            grid[i][j+1] = d
        if i-1 >=0 and grid[i-1][j] ==0:
            queue.append((i-1,j,d))
            grid[i-1][j] = d
        if i+1 <len(grid) and grid[i+1][j] ==0:
            queue.append((i+1,j,d))
            grid[i+1][j] = d
        if i-1 >=0 and j-1 >=0 and grid[i-1][j-1] ==0:
            queue.append((i-1,j-1,d))
            grid[i-1][j-1] = d
        if i+1 <len(grid) and j+1 <len(grid[0]) and grid[i+1][j+1] ==0:
            queue.append((i+1,j+1,d))
            grid[i+1][j+1] = d
        if i+1<len(grid) and j-1 >=0 and grid[i+1][j-1] ==0:
            queue.append((i+1,j-1,d))
            grid[i+1][j-1] = d
        if i-1 >=0 and j+1<len(grid[0]) and grid[i-1][j+1] ==0:
            queue.append((i-1,j+1,d))
            grid[i-1][j+1] = d
                        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.append((0,0,1))
        if grid[0][0] ==0:
            grid[0][0] =1
        else: return -1
        row_idx= len(grid)-1
        col_idx = len(grid[0])-1
        while queue:
            dt = queue.popleft()
            #print(dt)
            r,c,d = dt
            if r==row_idx and c == col_idx:
                return d
            self.enqueNeighbors(grid,queue,dt,row_idx,col_idx)
        print(len(queue))
        return -1
            
        