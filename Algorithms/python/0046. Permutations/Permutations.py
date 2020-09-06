class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #return permutations(nums)
        def permutation(n, output, nums):
            for i in range(n + 1):#n個長度間隔
                temp = output.copy()
                if i == len(nums) - 1:
                    temp.append(nums[n])
                else:
                    temp.insert(i, nums[n])#插入數字
                if len(temp) == len(nums):#若與nums等長，表示為一結果
                    self.res.append(temp)
                else:
                    permutation(n + 1, temp, nums)#繼續做下一個數字
            return
        if len(nums) <= 1:
            return [nums]
        self.res = []
        permutation(1, [nums[0]], nums)
        return self.res