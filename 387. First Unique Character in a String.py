class Solution:
    def firstUniqChar(self, s):
        h = {}
        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
        
        i = 0
        for c in s:
            if h[c] == 1: return i
            i += 1
        
        return -1
        # TIME complexity: O(N), have to scan the whole string
        # SPACE complexity: O(1), there can be maximum 26 elements in the dictionary

test = Solution()

s = "hi how are you"
print(test.firstUniqChar(s))