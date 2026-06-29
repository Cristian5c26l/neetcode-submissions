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
        
        head = linked_list_array[0]

        # O(n)
        for i in range(len(linked_list_array) - 1):
            linked_list_array[i].next = linked_list_array[i + 1]# Fundamental and basic operation to connect a node to another one in a linked list

        linked_list_array[-1].next = None

        return head

        