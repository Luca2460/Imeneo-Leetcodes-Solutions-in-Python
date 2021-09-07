from collections import deque
class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        q = deque()
        
        output = [[-1 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    q.append((i,j,0))
        
        while q:
            i,j,dist = q.popleft()
            
            if i+1 < m:
                if output[i+1][j] == -1:
                    output[i+1][j] = dist + 1
                    q.append((i+1,j,dist+1))
            if i-1 >= 0:
                if output[i-1][j] == -1:
                    output[i-1][j] = dist + 1
                    q.append((i-1,j,dist+1))
            if j+1 < n:
                if output[i][j+1] == -1:
                    output[i][j+1] = dist + 1
                    q.append((i,j+1,dist+1))
            if j-1 >= 0:
                if output[i][j-1] == -1:
                    output[i][j-1] = dist + 1
                    q.append((i,j-1,dist+1))
                    
        return output
                    
sol = Solution()

mat = [[0,0,0],[0,1,0],[1,1,1]]

print(sol.updateMatrix(mat))