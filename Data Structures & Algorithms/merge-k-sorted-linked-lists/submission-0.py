# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Brute Force or Intuitive Solution
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)

        def merge(nums, s, m, e):
            L = nums[s: m + 1]
            R = nums[m + 1: e + 1]

            i = 0
            j = 0
            k = s

            # Merge the two sorted halfs L and R
            while i < len(L) and j < len(R):# Modifying nums1 in-place 
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1

                k += 1

            while i < len(L):
                nums[k] = L[i]
                k += 1
                i += 1

            while j < len(R):
                nums[k] = R[j]
                k += 1
                j += 1

        def merge_sort(nums, s, e):
            if e - s + 1 <= 1:
                return

            m = (s + e) // 2

            merge_sort(nums, s, m)
            merge_sort(nums, m + 1, e)

            merge(nums, s, m, e)

        nums = []# all nums with n elements
        for lst in lists:
            curr = lst
            while curr:
                nums.append(curr.val)
                curr = curr.next

        merge_sort(nums, 0, len(nums) - 1)

        head = ListNode(-1)
        aux = head
        for n in nums:
            aux.next = ListNode(n)
            aux = aux.next

        return head.next






        