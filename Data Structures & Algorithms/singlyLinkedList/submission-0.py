class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.linked_list = ListNode(-1)
        self.tail = self.linked_list
        self.size = 0

    
    def get(self, index: int) -> int:
        if self.size == 0 or index < 0 or index >= self.size:# if i is out of bounds
            return -1

        curr = self.linked_list.next
        i = 0
        while curr:
            if i == index:
                return curr.val

            i += 1
            curr = curr.next

        return -1
        

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)

        if self.size == 0:
            self.tail = new_head

        new_head.next = self.linked_list.next
        self.linked_list.next = new_head
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.size += 1


    def remove(self, index: int) -> bool:
        if self.size == 0 or index < 0 or index >= self.size:
            return False

        i = 0
        curr = self.linked_list
        while curr:
            if i == index:
                curr.next = curr.next.next

                if i == self.size - 1:
                    self.tail = curr
                    
                return True

            i += 1
            curr = curr.next


        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.linked_list.next
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values

