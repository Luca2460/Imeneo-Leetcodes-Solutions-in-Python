class Solution:
    def subarraySum(self, nums, k): # had to look up the solution. This is translated from java
        hashmap = {0:1}
        s = 0
        res = 0
        
        for num in nums:
            s += num
            if s-k in hashmap: res += hashmap[s-k]
            if s in hashmap: hashmap[s] += 1
            else: hashmap[s] = 1

        return res
        # TIME complexity: O(N)
        # SPACE complexity: O(N)

test = Solution()
n = [1, -2, 4, 5, 12, -8, 1, 2, -1, -2]
k = 4

print(test.subarraySum(n, k))