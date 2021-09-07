from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]: # I came up with it myself
        m = len(image) - 1
        n = len(image[0]) - 1
        
        col = image[sr][sc]
        image[sr][sc] = newColor
        q = deque()
        q.append((sr,sc))
        
        seen = set() # One could avoid using a seen set as it's only needed if newColor == col, which is a case that could be treated separately

        while q:
            px,py = q.popleft()
            
            if (px+1, py) not in seen:
                if px+1 <= m:
                    if image[px+1][py] == col:
                        image[px+1][py] = newColor
                        q.append((px+1,py))
                        seen.add((px+1,py))
            if (px-1,py) not in seen:
                if px-1 >= 0:
                    if image[px-1][py] == col:
                        image[px-1][py] = newColor
                        q.append((px-1,py))
                        seen.add((px-1,py))
            if (px,py+1) not in seen:            
                if py+1 <= n:
                    if image[px][py+1] == col:
                        image[px][py+1] = newColor
                        q.append((px,py+1))
                        seen.add((px,py+1))
            if (px,py-1) not in seen:
                if py-1 >= 0:
                    if image[px][py-1] == col:
                        image[px][py-1] = newColor
                        q.append((px,py-1))
                        seen.add((px,py-1))
        return image

        # TIME complexity: O(N), we might have to visit every pixel
        # SPACE complexity: O(min(m,n)), max number of neighbors simultaneously in queue is 4*min(m,n)
                    