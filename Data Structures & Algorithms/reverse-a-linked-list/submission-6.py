# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brute Force solution (real reverse of nodes A -> B -> C -> Null to C -> B -> A -> None)
        # Time complexity: O(n)
        # Space complexity: O(n) (due to the creation of the auxiliar linked_list_array array)

        if head is None:
            return None
        
        # Traverse list (O(n))
        linked_list_array = []
        curr = head
        while curr:
            linked_list_array.append(curr)
            curr = curr.next

        linked_list_array.reverse()# O(n)
        
        dummy_node = ListNode(-1)
        curr = dummy_node

        # O(n)
        for node in linked_list_array:
            node.next = None
            curr.next = node
            curr = curr.next

        head = dummy_node.next

        return head

        