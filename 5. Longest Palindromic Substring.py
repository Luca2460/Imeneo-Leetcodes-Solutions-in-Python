class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0
        longest = s[0]
        
        for i in range(1, len(s)):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right-left > len(longest) - 1:
                        longest = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
                    
        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right-left > len(longest) - 1:
                        longest = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
                
        return longest

        # TIME complexity: O(N^2)
        # SPACE complexity: O(N)