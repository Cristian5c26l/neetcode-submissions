# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Optimal Solution
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # BFS
        queue = deque()# we use a queue to make the BFS Algorithm work successfully

        if root:
            queue.append(root)

        visible_nodes = [] # the nodes that are visible from the right side of the tree, ordered from top to bottom, are the last node (from left to right) of each level
        while len(queue) > 0:

            last_right_node = queue[0].val
            for _ in range(len(queue)):
                curr = queue.popleft()
                last_right_node = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            visible_nodes.append(last_right_node)

        return visible_nodes