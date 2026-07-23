class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.dyn_arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.dyn_arr[i]# O(1)


    def set(self, i: int, n: int) -> None:
        self.dyn_arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.dyn_arr[self.length] = n#O(1)
        self.length += 1


    def popback(self) -> int:
        last_arr_element = self.dyn_arr[self.length - 1]
        self.dyn_arr[self.length - 1] = 0
        self.length -= 1
        return last_arr_element
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.dyn_arr[i]

        self.dyn_arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
