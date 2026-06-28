# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        linked_list_array = []
        curr = head
        while(curr is not None):
            linked_list_array.append(curr.val)
            curr = curr.next

        linked_list_array.reverse()

        curr = head
        
        for val in linked_list_array:
            curr.val = val
            curr = curr.next

        return head

        