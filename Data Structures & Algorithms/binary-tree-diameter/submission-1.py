# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter = 0

    def helper(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.max_diameter

    
