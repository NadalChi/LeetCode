# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodes = [root]
        res = []
        while nodes:
            res.append([i.val for i in nodes])
            temp = [(i.left, i.right) for i in nodes]
            nodes = [j for i in temp for j in i if j]
        return res[::-1]
            