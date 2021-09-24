class Solution:
    def compress(self, chars):
        i = 1
        j = 1
        counter = 1
        
        l = len(chars)
    
        while j < l:
            if chars[j] == chars[j-1]:
                counter += 1
            else:
                if counter > 1:
                    for c in str(counter):
                        chars[i] = c
                        i += 1
                    counter = 1
                chars[i] = chars[j]               
                i += 1
            j += 1
            
        if counter > 1:
            for c in str(counter):
                chars[i] = c
                i += 1
            
        return i
        # TIME complexity: O(N)
        # SPACE complexity: O(1)

test = Solution()
s = ["a","a","a","b","b","a","a"]
print(test.compress(s))