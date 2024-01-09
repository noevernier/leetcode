# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):

            nonlocal res

            if not root:
                return 0, 0
            
            l_max_left, l_max_right = dfs(root.left)
            r_max_left, r_max_right = dfs(root.right)

            max_left, max_right = max(l_max_left, l_max_right) + 1, max(r_max_left, r_max_right) + 1
            res = max(res, max_left + max_right - 2)
            return max_left, max_right

        dfs(root)
        return res