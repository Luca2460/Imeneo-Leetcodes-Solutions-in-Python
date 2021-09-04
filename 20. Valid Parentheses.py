class Solution:
    def isValid(self, s):  # came up with this myself, but it was an 'easy' leetcode
        last_open = []
        
        matchings = set()
        matchings.add(("(",")"))
        matchings.add(("[","]"))
        matchings.add(("{","}"))
        
        for c in s:
            if c == "(" or c =="[" or c =="{":
                last_open.append(c)
            else:
                if last_open:                   
                    if (last_open.pop(), c) not in matchings:
                        return False
                else:
                    return False

        if not last_open:
            return True
        
        return False

        # time complexity: O(N)
        # space complexity: O(N) (O(N/2) actually, considering the worst case)
            
sol = Solution()

print(int(sol.isValid("{[](())}")))