class Solution:
    def removeDuplicates(self, nums):
        #return len(set(nums))# not in space
        if not nums:
            return 0
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                res += 1
                nums[res] = nums[i + 1]
        return res + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        