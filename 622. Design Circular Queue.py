class MyCircularQueue: 
    # I was given the name and parameters of each function and I had to implement them, 
    # the implementation has passed all of the testcases and has been accepted

    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = k
        self.head = 0
        self.tail = 0
        
        # Head is the index of the first element of the queue
        # Tail is the index of the first free spot available in the queue
        
        # If queue[head] == None, there is no element in the queue (empty)
        # If queue[tail] != None, there is no free spot in the queue (full)

    def enQueue(self, value: int) -> bool:
        if self.queue[self.tail] != None:
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size 
        return True

    def deQueue(self) -> bool:
        if self.queue[self.head] == None:
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        if self.queue[self.head] == None:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.queue[self.head] == None:
            return -1
        return self.queue[self.tail - 1]
        
    def isEmpty(self) -> bool:
        if self.queue[self.head] == None:
            return True
        return False

    def isFull(self) -> bool:
        if self.queue[self.tail] != None:
            return True
        return False

    # TIME complexity: Insertion O(1), Removal O(1)
    # SPACE complexity: O(N), N is the size of the queue
        


# Your MyCircularQueue object will be instantiated and called as such:

obj = MyCircularQueue(5)
param_1 = obj.enQueue(2)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()

print(param_2)