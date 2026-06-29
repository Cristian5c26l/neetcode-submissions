# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Optimal solution (real reverse of nodes A -> B -> C -> Null to C -> B -> A -> None)
        # Time complexity: O(n)
        # Space complexity: O(1)

        if head is None:
            return None
        
        prev = None
        curr = head

        while curr:# O(n)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev

        return head

        