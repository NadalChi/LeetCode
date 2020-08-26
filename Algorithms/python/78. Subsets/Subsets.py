class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            res += copy.deepcopy(res)
            for j in range(len(res)//2):
                res[j].append(nums[i])
        return res
        
            