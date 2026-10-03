# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if root is None:
            return 1
        
        self.output = 1
        def dfs(root):
            if root is None:
                return 0

            if root.left:
                if root.left.val >= root.val:
                    self.output += 1
                    dfs(root.left)
                else:
                    root.left.val = root.val
                    dfs(root.left)
            if root.right:
                if root.right.val >= root.val:
                    self.output += 1
                    dfs(root.right)
                else:
                    root.right.val = root.val
                    dfs(root.right)
            
        dfs(root)
            
        return self.output
            
