# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        output = []

        while queue:
            distance = len(queue)

            for i in range(distance):
                node = queue.popleft()
                rightnode = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            output.append(rightnode.val)
        
        return output