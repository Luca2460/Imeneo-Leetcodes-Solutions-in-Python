class Solution:
    def addBinary(self, a: str, b: str) -> str: # I came up with it, it's very memory efficient yet very slow
        a = int(a)
        b = int(b)
        s = a+b

        for i in range(len(str(s))):
            if s % 10**(i+1) / 10**i >= 2:
                s -= 2*10**i
                s += 10**(i+1)
        return str(s)

        # TIME complexity: O(N), N is the length of the sum
        # SPACE complexity: O(N)