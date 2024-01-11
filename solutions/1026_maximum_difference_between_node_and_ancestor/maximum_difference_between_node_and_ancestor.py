# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def bfs(root):

            nonlocal res

            if not root:
                return 10e5, 0
            l_min_elem, l_max_elem = bfs(root.left)
            r_min_elem, r_max_elem = bfs(root.right)

            min_val, max_val = min(min(l_min_elem, r_min_elem), root.val), max(max(l_max_elem, r_max_elem), root.val)

            res = max(res, max(abs(root.val - min_val), abs(root.val - max_val)))

            return min_val, max_val

        bfs(root)
        return res