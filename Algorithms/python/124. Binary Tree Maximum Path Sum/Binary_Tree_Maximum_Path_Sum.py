# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def pathSum(root):
            if not root:
                return 0
            if root not in self.dict:
                self.dict[root] = root.val + max(0, pathSum(root.left), pathSum(root.right))
                self.res = max(self.res, root.val + max(0, pathSum(root.left)) + max(0, pathSum(root.right)))
            return self.dict[root]
        self.dict = {}
        self.res = -float('Inf')
        pathSum(root)
        return self.res