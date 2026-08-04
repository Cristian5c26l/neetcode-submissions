# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def min_value_node(root):
            curr = root
            while curr and curr.left:
                curr = curr.left

            return curr

        # Time Complexity: O(logn) if tree root is balanced
        def remove(root, val):# Deliver the updated root
            if not root:
                return None

            if val > root.val:
                root.right = remove(root.right, val)
            elif val < root.val:
                root.left = remove(root.left, val)
            else:# val == root.val
                if not root.right:# node root has 0 or 1 child (right or left)
                    return root.left
                elif not root.left:
                    return root.right
                else:# node root has 2 childs (right and left). Replace node root with the min node of its right subtree (root.right) to keep the fundamental BST property
                    node = min_value_node(root.right)
                    root.val = node.val
                    root.right = remove(root.right, node.val)


            return root

        return remove(root, key)

        