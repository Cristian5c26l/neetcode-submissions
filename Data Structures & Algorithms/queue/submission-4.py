class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None# Due to the pop operation
        self.next = None

class Deque:
    
    def __init__(self):
        self.queue = ListNode(-1)# -1 is a dummy node
        self.tail = self.queue
        self.size = 0


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = self.tail.next
        self.size += 1

    def appendleft(self, value: int) -> None:# insert at head in Doubly Linked List
        new_first_node = ListNode(value)
        new_first_node.prev = self.queue

        if self.size == 0:
            self.tail = new_first_node

        new_first_node.next = self.queue.next

        if self.queue.next:# Guessing that current queue is self.queue = -1 -> None (where self.queue.next is None)
            self.queue.next.prev = new_first_node

        self.queue.next = new_first_node# append left
        self.size += 1

    def pop(self) -> int:
        
        if self.isEmpty():
            return -1
        
        popped = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return popped

    def popleft(self) -> int:# Before the popleft, suppose queue = -1 -> 2 -> None, where queue.next (original queue) is 2 -> None 

        if self.isEmpty():
            return -1

        popped = self.queue.next.val
        self.queue.next = self.queue.next.next# pop left
        self.size -= 1

        if self.queue.next:# if queue is not empty
            self.queue.next.prev = self.queue
        else:# here queue (self.queue.next) is none (queue is empty)
            self.tail = self.queue
        
        
        return popped
