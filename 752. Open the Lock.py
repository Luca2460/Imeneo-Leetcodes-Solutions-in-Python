from collections import deque

class Solution:             # came up with it myself, except for the usage of yield in the neighbors function
    def neighbors(self, s):
        res = []
        for i in range(4):
            for d in (-1, 1):
                yield s[:i] + str((int(s[i])+d)%10) + s[i+1:]

        
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if "0000" in deadends: return -1
        seen = set()
        
        q = deque()
        q.append(('0000', 0))
        seen.add("0000")
        
        while q:
            curr, depth = q.popleft()
            if curr == target: return depth
            nn = self.neighbors(curr)
            for n in nn:
                if n not in seen and n not in deadends:
                    q.append((n,depth+1))
                    seen.add(n)
        return -1


sol = Solution()

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

print(sol.openLock(deadends, target))