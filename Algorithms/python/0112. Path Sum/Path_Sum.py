# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left and self.hasPathSum(root.left, sum - root.val) == True:
            return  True
        if root.right and self.hasPathSum(root.right, sum - root.val) == True:
            return True
        if root.left == None and root.right == None and sum == root.val:
            return True
        return False
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        