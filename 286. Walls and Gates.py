from collections import deque

class Solution:
    def wallsAndGates(self, rooms):  # for some reasons its extremely slow (like ~ 20 times slower than it should)
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        
        m = len(rooms)
        if m ==0: return
        n = len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        k = -1
        curr = (0,0)
        while queue:
            k += 1 # probably this usage of k, rather than storing k inside of each element of the queue, somehow slows things down, 
                   # perhaps because we end up processing stuff twice
            for i in range(len(queue)):
                curr = queue.popleft()
                if rooms[curr[0]][curr[1]] > k:
                    rooms[curr[0]][curr[1]] = k
                    # add neighbors
                for direction in directions:
                    r = curr[0] + direction[0]
                    c = curr[1] + direction[1]
                    if r >= 0 and r < m and c >= 0 and c < n:
                        if rooms[r][c] > k +1:
                            queue.append((r,c))


sol = Solution()

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

expectedSol = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

sol.wallsAndGates(rooms) # changes turns the rooms variable into the solution
print(rooms)
print(expectedSol)