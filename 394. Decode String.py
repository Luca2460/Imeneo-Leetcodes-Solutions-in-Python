class Solution:
    def decodeString(self, s: str) -> str:
        
        nums = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        coeff = ""

        stack = []
        s = s + "-"  
        i = 0
        
        startNum = -1
        while s[i] != "-":
            if s[i] in nums and startNum==-1:
                startNum = i
            elif s[i] == "[":
                stack.append(startNum)
                stack.append(i)
                startNum = -1
            elif s[i] == "]":
                p = stack.pop()
                n = stack.pop()
                num = int(s[n:p])
                s = s[:n] + num*s[p+1:i] + s[i+1:]
                i+= (num-1)*(i-p-1) - 2 - (p-n)
            i += 1
            
        return s[:-1]
        
sol = Solution()

s = "10[a]3[b]"

print(sol.decodeString(s))