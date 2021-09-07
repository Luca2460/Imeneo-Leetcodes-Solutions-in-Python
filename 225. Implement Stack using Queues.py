from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        while self.q[0] != x:
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return bool(not self.q)

stack = MyStack()

stack.push(4)
stack.push(3)
stack.push(7)
stack.pop()
print(stack.top())
stack.push(1)

while not stack.empty():
    print(stack.pop())
