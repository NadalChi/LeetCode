# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if nums == []:
            return []
        root = nums[int(len(nums)/2)]
        tree = TreeNode(root)
        if int(len(nums)/2) > 0:
            tree.left = self.sortedArrayToBST(nums[:int(len(nums)/2)])
        if len(nums) - 1 - int(len(nums)/2) > 0:
            tree.right = self.sortedArrayToBST(nums[int(len(nums)/2) + 1:])
        #print(root)
        return tree
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        