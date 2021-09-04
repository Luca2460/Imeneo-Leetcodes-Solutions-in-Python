from collections import deque
import math

class Solution: # came up with it myself
    def neighbors(self, n):
        for i in range(1, int(math.sqrt(n))+1):
            yield n - i*i
        
    def numSquares(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2: return n
        
        q = deque()
        q.append((n, 0))
        seen = set()
        seen.add(n)
        
        while q:
            node, depth = q.popleft()
            
            for i in self.neighbors(node):
                if i == 0: return depth + 1
                if i not in seen:
                    seen.add(i)
                    q.append((i, depth+1))

    # time complexity: O((sqrt(n)^(h+1)-1)/(sqrt(n)-1)) = O(sqrt(n)^h) where h is the maximum output; this is the number of nodes
    # space complexity: O(sqrt(n)^h); 


sol = Solution()

print(sol.numSquares(5))