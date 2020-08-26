# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []
        inorder = []
        self.inorder_(root, inorder)
        return inorder
    def inorder_(self, parent, ans):
        if parent.left != None:
            self.inorder_(parent.left, ans)
        ans.append(parent.val)
        #print(ans)
        if parent.right != None:
            self.inorder_(parent.right, ans)
        return ans
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        