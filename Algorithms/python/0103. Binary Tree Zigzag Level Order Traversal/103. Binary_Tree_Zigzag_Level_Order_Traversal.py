# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        temp = []
        roots = []
        roots.append(root)
        ans = []
        if root == None:
            return ans
        for i in range(0,len(roots)):
            temp.append(roots[i].val)
        ans.append(temp)        
        self.bfs(roots,ans)
        print(ans)
        for i in range (0,len(ans)):
            if i % 2 == 1:
                ans[i] = list(reversed(ans[i]))
        return ans
    def bfs(self, parents,ans):
        roots = []
        for i in range(0,len(parents)):
            if parents[i].left != None:
                roots.append(parents[i].left)
            if parents[i].right != None:
                roots.append(parents[i].right)
        if len(roots) == 0:
            return ans
        temp = []
        for i in range(0,len(roots)):
            temp.append(roots[i].val)
        ans.append(temp)
        self.bfs(roots,ans)
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        