# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Optimal Solution
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # Breadth First Search (BFS) Algorithm is an algorithm that traverses the tree level by level (left to right in each level of the tree), rather than going deeper into the tree (DFS)
        queue = deque()
        if root:
            queue.append(root)# append to the final

        res = []# each sublist contains the values of nodes at a particular level in the tree, from left to right.
        #level = 0
        while len(queue) > 0:# here, len(queue) is actually the current length of the queue
            #print("level: ", level)
            level_nodes = []
            for _ in range(len(queue)):# here, len(queue) is a snapshot of the current length of the queue
                curr = queue.popleft()
                level_nodes.append(curr.val)# print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(level_nodes)
            #level += 1

        return res
            


         
        