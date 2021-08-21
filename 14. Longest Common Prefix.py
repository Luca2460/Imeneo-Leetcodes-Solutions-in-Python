class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str: # I came up with it myself, however, there was no special DS or algorithm involved
        shortest = min(strs, key=len)
        # vertical scanning
        for i in range(len(shortest)):
            for s in strs:
                if shortest[:i + 1] != s[:i + 1]: # first i in the for loop is i=0. which is useless
                    return shortest[:i]
        return shortest

        # TIME complexity: O(L*N), where L is the length of the longest common prefix and N is the number of strings in the list
        # alternatively, time complexity is O(S) where S is the total number of character in the list

        # SPACE complexity: O(1)

strs = ["flower", "flaw", "flute"]

print(Solution.longestCommonPrefix(Solution, strs))