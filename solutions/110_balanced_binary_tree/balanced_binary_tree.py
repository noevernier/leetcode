# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0, 0, True
            
            l_depth_left, l_depth_right, l_balanced = dfs(root.left)
            r_depth_left, r_depth_right, r_balanced = dfs(root.right)

            depth_left = max(l_depth_left, l_depth_right) + 1
            depth_right = max(r_depth_left, r_depth_right) + 1

            return depth_left, depth_right,r_balanced and l_balanced and abs(depth_left - depth_right) <= 1

        _, _, res = dfs(root)
        return res