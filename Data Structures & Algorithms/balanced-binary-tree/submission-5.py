# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        is_balanced = [True]

        def height(root):
            if not root:
                return 0

            if not root.right:# 0 or 1 child
                return 1 + height(root.left)
            elif not root.left:
                return 1 + height(root.right)
            else:# 2 children
                true_height = max(1 + height(root.left), 1 + height(root.right))
                return true_height

        def check_is_balanced(root, is_balanced):

            if not root:
                return

            
            check_is_balanced(root.left, is_balanced)

            if is_balanced[0] == False:
                return

            print(root.val)
            left_height = height(root.left)
            right_height = height(root.right)
            is_balanced[0] = abs(left_height - right_height) <= 1
            print(f"root val: {root.val}. left height: {left_height}. right height: {right_height}. is balanced: {is_balanced[0]}")
            #if is_balanced[0] == False:
            #    return
            check_is_balanced(root.right, is_balanced)

        check_is_balanced(root, is_balanced)
        return is_balanced[0]
         
        