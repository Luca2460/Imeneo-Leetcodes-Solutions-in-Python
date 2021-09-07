class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        if not rooms:
            return True
        
        n = len(rooms)
        seen = set()

        stack = [0]
        
        while stack:
            key = stack.pop()
            if key not in seen:
                seen.add(key)
                for i in rooms[key]:
                    if i not in seen:
                        stack.append(i)
        return not bool(n - len(seen))
        
    # TIME complexity: O(N+E), where N is the total number of rooms and E the total number of keys (E might be <,>,= than N),
    # SPACE complexity: O(N)

sol = Solution()
rooms = [[1],[2],[3],[]]

print(sol.canVisitAllRooms(rooms))