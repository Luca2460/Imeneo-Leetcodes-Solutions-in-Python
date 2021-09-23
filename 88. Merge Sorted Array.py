class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        pointer = 0
        
        for i in range(m):
            while pointer < n and nums2[pointer]<nums1[i]:
                res.append(nums2[pointer])
                pointer += 1
            res.append(nums1[i])
        
        while pointer < n:
            res.append(nums2[pointer])
            pointer += 1    
            
        nums1 = res            
        print(nums1)
        # TIME complexity: O(n+m)
        # SPACE complexity: O(n+m)

test = Solution()
a1 = [1,2,2,4,7,8,8]
m = 7
a2 = [3,5,6,9,10]
n = 5

test.merge(a1,m,a2,n)