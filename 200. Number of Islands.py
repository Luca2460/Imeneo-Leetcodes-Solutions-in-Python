from collections import deque

class Solution:
    def numIslands(self, grid): # came up with it myself (but I received the hint of markin a visited island with "0")
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        res = 0
        for  i in range(m):
            for j in range(n):
                if grid[i][j] == "1": # when an Island is found, trigger BFS (or DFS) to find its extension
                    q.append([i,j])
                    grid[i][j] = "0"
                    res += 1
                    while q: # BFS here
                        [x, y] = q.popleft()
                        if x + 1 < m:
                            if grid[x+1][y] == "1":
                                grid[x+1][y] = "0"
                                q.append([x+1, y])
                        if y + 1 < n:
                            if grid[x][y+1] == "1":
                                grid[x][y+1] = "0"
                                q.append([x,y+1])
                        if x - 1 >= 0:
                            if grid[x-1][y] == "1":
                                grid[x-1][y] = "0"
                                q.append([x-1, y])
                        if y - 1 >= 0:
                            if grid[x][y-1] == "1":
                                grid[x][y-1] = "0"
                                q.append([x,y-1])  
        return res

        # Time complexity: O(NxM), because we need to process each square. 
        # Space complexity: O(min(N,M)), because in the worst case, the perimeter of the visited portion of the island (i.e.
        #  the length of the queue) will be 2*min(N,M)

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

sol = Solution()

print(sol.numIslands(grid))