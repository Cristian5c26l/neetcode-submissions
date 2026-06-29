# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force Solution
        # Time Complexity: O((n + m)^2) (due to bubble sort algorithm)
        # Space Complexity: O(n + m) (due to auxiliar array = [])

        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # Link the end of the list1, to the list2
        curr = list1
        while curr.next:
            curr = curr.next

        curr.next = list2

        # Add all ListNodes to an array
        array_list = []
        curr = list1
        while curr:
            #print(curr.val)
            array_list.append(curr)
            curr = curr.next

        # Sort array with bubble sort algorithm (O(n+m)*(n+m))
        for i in range(len(array_list)):
            for j in range(len(array_list) - i - 1):
                if array_list[j].val > array_list[j + 1].val:
                    array_list[j + 1], array_list[j] = array_list[j], array_list[j + 1]# swap
        # array_list.sort(key=lambda node: node.val)

        # Build sorted  list sorted
        sorted_merged_list = array_list[0]
        for i in range(len(array_list) - 1):
            array_list[i].next = array_list[i + 1] # Fundamental and basic operation to connect a node to another one in a linked list

        array_list[-1].next = None# Finish up the list

        return sorted_merged_list
        