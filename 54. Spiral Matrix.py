class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        imin = 0
        imax = len(matrix)
        jmin = 0
        jmax = len(matrix[0])
        
        res = []  
        
        while imax>imin and jmax>jmin:
            for j in range(jmin,jmax):
                res.append(matrix[imin][j])
            for i in range(imin+1,imax):
                res.append(matrix[i][jmax-1])
            if imin+1 != imax:
                for j in range(jmax-2, jmin-1, -1):
                    res.append(matrix[imax-1][j])
            if jmax-2 != jmin-1:
                for i in range(imax-2,jmin, -1):
                    res.append(matrix[i][jmin])
            imin +=1
            jmin += 1
            imax -= 1
            jmax -= 1
        
        return res
        # TIME complexity: O(N), as we have to add each value from the matrix
        # SPACE complexity: O(1) without the result, O(N) including the result.

test = Solution()

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(test.spiralOrder(matrix))