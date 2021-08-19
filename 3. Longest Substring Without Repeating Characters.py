def lengthOfLongestSubstring(s: str) -> int:
    hashmap = {}
    longest = 0
    start = 0
    i=0

    for j in range(len(s)):
        while s[j] in hashmap:
            del hashmap[s[i]]
            i = i+1
            start = i
        hashmap[s[j]] = j
        longest = max(longest, j-start+1)
    return longest

s = "abccd"

print(lengthOfLongestSubstring(s))