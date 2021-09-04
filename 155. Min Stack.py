class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack: # if stack is empty
            self.stack.append((val, val))
            return
        
        curr_min = self.stack[-1][1]
        self.stack.append((val, min(val, curr_min)))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:     # time complexity: O(1) 
        return self.stack[-1][1] # space complexity: O(n)
                                

        


obj = MinStack()
obj.push(4)
obj.pop()
obj.push(4)
obj.push(2)
obj.push(12)
param_3 = obj.top()
param_4 = obj.getMin()

print(param_4)