# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        else:
            return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        if left.val == right.val:
            a = self.compare(left.left, right.right)
            b = self.compare(left.right, right.left)
            return a and b
        else:
            return False
        
        
        
#         if not root:
#             return True
#         elif not root.left and not root.right:
#             return True
#         elif not root.left or not root.right:
#             return False
#         elif root.left.val == root.right.val:
#             return self.compare(root.left, root.right)
#         else:
#             return False
#     def compare(self, left, right):
        
#         if not left.left and not right.right:
#             pass
#         elif not left.left or not right.right:
#             return False
#         elif left.left.val != right.right.val:
#             return False
#         else:
#             return self.compare(left.left, right.right)
        
#         if not left.right and not right.left:
#             pass
#         elif not left.right or not right.left:
#             return False
#         elif left.right.val != right.left.val:
#             return False
#         else:
#             return self.compare(left.right,right.left)
        
            
            
        """
        :type root: TreeNode
        :rtype: bool
        """
        