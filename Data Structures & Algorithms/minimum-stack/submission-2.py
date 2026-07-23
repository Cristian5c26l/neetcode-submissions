class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)#O(1)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return

        #self.min_stack.pop()#O(1)
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]# O(1)

    def getMin(self) -> int:
        return self.min_stack[-1]
        
