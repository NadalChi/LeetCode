# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # inorder = [] #inorder 為全域變數
    # def isValidBST(self, root):
    #     if root == None:
    #         return True
    #     if root.left != None:
    #         self.isValidBST(root.left)
    #     self.inorder.append(root.val)
    #     if root.right != None:
    #         self.isValidBST(root.right)
    #     print(self.inorder,len(self.inorder)-1)
    #     for i in range(len(self.inorder)-1):
    #         if self.inorder[i] >= self.inorder[i+1]:
    #             return False
    #     return True
    def isValidBST(self, root):
        if root == None:
            return True
        inorder = []
        self.inorder_(root, inorder)
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True
    def inorder_(self, parent, ans):
        if parent.left:
            self.inorder_(parent.left, ans)
        ans.append(parent.val)
        #print(ans)
        if parent.right:
            self.inorder_(parent.right, ans)
        return ans
        """
        :type root: TreeNode
        :rtype: bool
        """
        