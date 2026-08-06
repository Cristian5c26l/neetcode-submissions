# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # In order approach has O(n) time complexity, where n is the number of nodes in the given tree

        def findBSTKthSmallest(root, kth_smallest):# In order approach. Returns the KthSmallest and k counter. The main idea is start on the left SUBTREE to find the kth smallest element of the binary tree. We start on the left subtree due to the binary tree is a BST. A BST has the smallest value on the left subtree deepest.
            
            if not root:
                return

            findBSTKthSmallest(root.left, kth_smallest)# Left Subtree
            # Current Tree or node "root"

            if kth_smallest[1] == k:
                return

            kth_smallest[1] += 1
            #print(root.val)
            if kth_smallest[1] == k:
                kth_smallest[0] = root.val
                return
            #print(kth_smallest[1])
            findBSTKthSmallest(root.right, kth_smallest)# Right Subtree

        kth_smallest = [0, 0]# kthSmallest, k counter
        findBSTKthSmallest(root, kth_smallest)
        return kth_smallest[0]