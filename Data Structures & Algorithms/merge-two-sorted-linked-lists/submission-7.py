# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Optimal Solution
        # Time Complexity: O((n + m))
        # Space Complexity: O(1)

        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        dummy_node = ListNode(-1)
        merged_sorted_linked_list = dummy_node
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                next_curr1 = curr1.next
                curr1.next = None

                dummy_node.next = curr1# Fundamental operation to connect a node to another one
                dummy_node = dummy_node.next

                curr1 = next_curr1

            else:# curr2.val < curr1.val
                next_curr2 = curr2.next
                curr2.next = None
                
                dummy_node.next = curr2# Fundamental operation to connect a node to another one
                dummy_node = dummy_node.next

                curr2 = next_curr2

            
        if curr2:
            dummy_node.next = curr2
        elif curr1:
            dummy_node.next = curr1
                


        return merged_sorted_linked_list.next
        