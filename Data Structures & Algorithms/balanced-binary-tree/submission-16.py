# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Optimal Solution
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        def check_is_balanced(root):# Post Order Approach, which is O(n)

            if not root:# no tree
                return True, 0
            #elif not root.left and not root.right:# 0 children of a tree node
            #    return True, 1           

            is_balanced_left, h_left = check_is_balanced(root.left)
            
            if not is_balanced_left:
                return False, h_left

            is_balanced_right, h_right = check_is_balanced(root.right)

            if not is_balanced_right:
                return False, h_right

            is_balanced = abs(h_left - h_right) <= 1
            h = 1 + max(h_left, h_right)# h es la altura del "arbol" o root actual (contabilizando el nodo actual root, que es padre de root.left y root.right. Dicho nodo padre recibe informacion de la recursion check_is_balanced)

            return is_balanced, h

        return check_is_balanced(root)[0]
         
        