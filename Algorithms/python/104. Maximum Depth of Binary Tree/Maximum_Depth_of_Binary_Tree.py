# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        return self.search(root,1)
    def search(self, parent, max_len):
        level = max_len
        #print(parent.val, max_len)
        if parent.left != None:
            max_len += 1
            max_len = self.search(parent.left,max_len)
        max_len1 = level
        if parent.right != None:
            max_len1 += 1
            max_len1 = self.search(parent.right,max_len1)
        if parent.left == None and parent.right == None:
            #print('end')
            return max_len
        #print(parent.val,max_len,max_len1)
        return max_len if max_len > max_len1 else max_len1
        """
        :type root: TreeNode
        :rtype: int
        """
        