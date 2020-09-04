class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp = nums[i] if nums[i] > temp + nums[i] else temp + nums[i]
            res = res if res > temp else temp
        return res