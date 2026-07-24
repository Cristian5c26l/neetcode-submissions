class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.linked_list = ListNode(-1)
        self.size = 0
        self.tail = self.linked_list.next#
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size or self.size == 0:
            return -1
        
        curr = self.linked_list.next
        i = 0
        while curr:# For or traversing a LinkedList
            if i == index:
                return curr.val

            i += 1
            curr = curr.next
        
        return -1


    def addAtHead(self, val: int) -> None:
        curr = self.linked_list.next
        new_node = ListNode(val)
        new_node.next = curr
        self.linked_list.next = new_node

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        
        curr = self.linked_list
        while curr.next:
            curr = curr.next

        curr.next = ListNode(val)# Form of adding the next ListNode of a ListNode
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
                new_node.next = next_node
                curr.next = new_node
                break

            i += 1
            curr = curr.next

        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or self.size == 0:
            return

        curr = self.linked_list# -1 -> 8 -> None
        i = 0
        while curr:
            if i == index:
                curr.next = curr.next.next# Form of removing a ListNode from the Linked List
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