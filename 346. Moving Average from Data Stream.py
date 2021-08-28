class MovingAverage: # I came up with a solution but it was much slower, the next() function was O(N) instead of O(1) (I didnt use the window_sum variable)

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = [0] * size
        self.size = size
        self.head = 0 # no need for both head and tail since the sliding window is always full
        self.window_sum = 0
        self.count = 0
    

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum + val - self.queue[tail]
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)

            


obj = MovingAverage(5)
print(obj.next(2))
print(obj.next(1))
print(obj.next(21))
print(obj.next(56))
