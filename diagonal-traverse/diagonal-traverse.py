class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_size = len(mat)
        col_size = len(mat[0])
        edge_c = []
        for i,row in enumerate(mat):
            edge_c.append((i,0))
        for j in range(1,len(row)):
            edge_c.append((i,j))
        diagonals = []
        for headc in edge_c:
            x,y = headc
            diag = []
            while (x>=0 and x<row_size) and  (y>=0 and y<col_size):
                diag.append(mat[x][y])
                x-=1
                y+=1
            diagonals.append(diag)
        for i,diagonal in enumerate(diagonals):
            if i%2 !=0:
                copyd = diagonal[::-1]
                diagonals[i] = copyd
        res = []
        for diagonal in diagonals:
            for d in diagonal:
                res.append(d)
        return(res)
            
        