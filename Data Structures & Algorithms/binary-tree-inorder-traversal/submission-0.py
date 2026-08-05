# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root, nodes):# O(n)
            if not root:
                return

            inorder(root.left, nodes)
            nodes.append(root.val)# O(1)
            inorder(root.right, nodes)
        
        nodes = []
        inorder(root, nodes)
        return nodes