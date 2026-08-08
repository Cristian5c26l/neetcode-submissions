# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        i = 0# i-th node to build
        inorder_indices ={val: idx for idx, val in enumerate(inorder)}

        # Optimal Solution
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        def build_binary_tree(l, r):# Build Tree with time complexity O(n)
            nonlocal i, inorder_indices
            if l > r:
                return None

            root_val = preorder[i]
            root_node = TreeNode(root_val)

            #j = inorder.index(root_val)# Search Linear with time complexity O(n), where n are the total of nodes. j must to be between l and r
            j = inorder_indices[root_val]

            i += 1

            root_node.left = build_binary_tree(l, j - 1)
            root_node.right = build_binary_tree(j + 1, r)

            return root_node

        return build_binary_tree(0, len(inorder) - 1)