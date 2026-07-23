class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)#O(1)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return

        self.stack.pop()# O(1)
        

    def top(self) -> int:
        return self.stack[-1]# O(1)

    def getMin(self) -> int:# O(n), where n is the maximum number of elements present in the stack.

        min_value = (2 ** 31) - 1
        for element in self.stack:
            min_value = min(min_value, element)

        return min_value
        
