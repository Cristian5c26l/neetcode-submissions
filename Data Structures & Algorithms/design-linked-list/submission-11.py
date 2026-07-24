class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.linked_list = ListNode(-1)
        self.size = 0
        self.tail = self.linked_list
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size or self.size == 0:
            return -1
        
        curr = self.linked_list.next
        i = 0
        while curr:# Form of traversing a LinkedList
            if i == index:
                return curr.val

            i += 1
            curr = curr.next
        
        return -1


    def addAtHead(self, val: int) -> None:
        #curr = self.linked_list.next
        new_node = ListNode(val)
        new_node.prev = self.linked_list
        new_node.next = self.linked_list.next # self.linked_list.next is None at the beginning

        if new_node.next:
            new_node.next.prev = new_node

        self.linked_list.next = new_node

        if self.size == 0:# is the same as if self.tail.val == -1 and (self.linked_list.next is None):# if Linked List is empty (linked_list.next is the real linked list)
            self.tail = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:

        new_last_node = ListNode(val)
        new_last_node.prev = self.tail
        self.tail.next = new_last_node# Form of adding the next ListNode of a ListNode
        self.tail = self.tail.next# Jumping to the next ListNode

        self.size += 1        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == self.size:
            self.addAtTail(val)
            return

        curr = self.linked_list# -1 -> 1 -> 3 -> None
        i = 0
        while curr:

            if i == index:
                next_node = curr.next
                new_node = ListNode(val)
                new_node.prev = curr
                new_node.next = next_node

                next_node.prev = new_node
                curr.next = new_node
                break

            i += 1
            curr = curr.next

        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or self.size == 0:
            return

        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        curr = self.linked_list# -1 -> 8 -> None
        i = 0
        while curr:
            if i == index:
                curr.next = curr.next.next# Form of removing a ListNode from the Linked List
                curr.next.prev = curr
                break

            i += 1
            curr = curr.next

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)