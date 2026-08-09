# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def is_there_path_equal_to_sum(root, path_sum):# Time Complexity: O(n). Test with the root root = [1,3,2] and targetSum = 3, which shows the entire backtracking (based on DFS) of is_there_path_equal_to_sum

            if not root:# Base Case 1 (if no root, the tree has n a root-to-leaf path such that adding up all the values along the path equals targetSum )
                return False

            path_sum += root.val

            if not root.left and not root.right:# Base Case 2 (if the root is a leaf node and the current pah_sum is equal to the targetSum)
                return path_sum == targetSum
            if is_there_path_equal_to_sum(root.left, path_sum):
                return True
            if is_there_path_equal_to_sum(root.right, path_sum):
                return True

            #path_sum -= root.val# Explicit Backtracking
            return False

        return is_there_path_equal_to_sum(root, 0)


            