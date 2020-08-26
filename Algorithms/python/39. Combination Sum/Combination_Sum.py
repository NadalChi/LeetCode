class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates,target,0,[],res)
        return res
    def dfs(self,candidates,target,index,path,res):
        #print(candidates,target,index,path,res)
        if target == 0:
            #print('k')
            res.append(path)
            return
        if candidates[index] > target:
            return
        
        for i in range(index,len(candidates)):
            self.dfs(candidates,target-candidates[i],i,path+[candidates[i]],res)
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        