class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates,target,0,[],res)
        ans= []
        for i in range(0,len(res)):
            if res[i] not in ans:
                ans.append(res[i])
        return ans
    def dfs(self,candidates,target,index,path,res):
        #print(candidates,target,index,path,res)
        if target == 0:
            #print('k')
            res.append(path)
            return
        if index != len(candidates) and candidates[index] > target:
            return
        
        for i in range(index,len(candidates)):
            self.dfs(candidates,target-candidates[i],i+1,path+[candidates[i]],res)
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        