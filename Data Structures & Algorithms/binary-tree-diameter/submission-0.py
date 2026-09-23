# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # Update the global maximum diameter passing through the current node
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of subtree rooted at 'node'
            return 1 + max(left_height, right_height)
        
        get_height(root)
        return self.max_diameter