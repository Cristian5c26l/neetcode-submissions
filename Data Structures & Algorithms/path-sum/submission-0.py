# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        path_sum = 0

        def is_there_path_equal_to_sum(root):
            nonlocal path_sum

            if not root:# Base Case 1
                return False

            path_sum += root.val

            if not root.left and not root.right and path_sum == targetSum:# Base Case 2
                return True
            if is_there_path_equal_to_sum(root.left):
                return True
            if is_there_path_equal_to_sum(root.right):
                return True

            path_sum -= root.val
            return False

        return is_there_path_equal_to_sum(root)


            