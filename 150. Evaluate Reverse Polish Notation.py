class Solution:
    def evalRPN(self, tokens): # came up with it myself
        operations = {"+", "-", "*", "/"}
        
        stack = []
        
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            elif token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                res =  first - second
                stack.append(res)
            elif token == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                res =  first / second
                stack.append(int(res))
                
        return int(stack.pop())

        # time complexity: O(N)
        # space complexity: O(N) worst case, when half the input needs to be pushed into the stack and all the operations are in the bottom of the input


sol = Solution()

print(sol.evalRPN(tokens = ["4","13","5","/","+"]))
