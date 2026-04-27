class MinStack:

    def __init__(self):
        # stack = {}
        self.stack = []
        self.minHeap = collections.deque()
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minHeap:
            self.minHeap.append(val)
        else:
            if self.minHeap[-1] >= val:
                self.minHeap.append(val)


    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.minHeap[-1]:
            self.minHeap.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHeap[-1]
        
