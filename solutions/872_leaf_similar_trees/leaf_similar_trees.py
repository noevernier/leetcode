# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leafList(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]

            left_leaf = leafList(root.left)
            leaf_right = leafList(root.right)

            return left_leaf + leaf_right

        return leafList(root1)==leafList(root2)