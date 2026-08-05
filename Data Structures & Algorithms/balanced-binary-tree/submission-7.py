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
        # Space Complexity: O(1)

        def check_is_balanced(root):# In Order Approach, which is O(n)

            if not root:# no tree
                return True, 0
            elif not root.left and not root.right:# 0 children of a tree node
                return True, 1           

            is_balanced_left, h_left = check_is_balanced(root.left)# 1 (n2)
            
            if not is_balanced_left:
                return False, h_left

            is_balanced_right, h_right = check_is_balanced(root.right)#  1 (n3) + (1 (n4) + 1 + 0) (left n3 = 2) + (0) (right n3 = 0)

            if not is_balanced_right:
                return False, h_right

            is_balanced = abs(h_left - h_right) <= 1
            h = 1 + max(h_left, h_right)

            return is_balanced, h

        return check_is_balanced(root)[0]
         
        