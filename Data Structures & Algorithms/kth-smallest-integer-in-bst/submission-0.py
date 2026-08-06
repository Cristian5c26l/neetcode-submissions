# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findBSTKthSmallest(root, kth_smallest):# in order approach. Returns the KthSmallest k counter
            
            if not root:
                return

            findBSTKthSmallest(root.left, kth_smallest)
            
            if kth_smallest[1] == k:
                return
            
            kth_smallest[0] = root.val
            kth_smallest[1] += 1
            findBSTKthSmallest(root.right, kth_smallest)

        kth_smallest = [0, 0]# kthSmallest, k counter
        findBSTKthSmallest(root, kth_smallest)
        return kth_smallest[0]