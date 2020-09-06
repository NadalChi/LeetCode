class Solution:
    def searchInsert(self, nums, target):
    #     if target > nums[-1]:
    #         return len(nums)
    #     if target < nums[0]:
    #         return 0
    #     return self.binary(nums, int((len(nums)-1)/2), int((len(nums)+1)/2), target)
    # def binary(self, nums, pos, double, target):
    #     print(target, pos, double)
    #     if target == nums[pos]:
    #         return pos
    #     if double <= 1:
    #         return pos if nums[pos] > target else pos + 1
    #     pos = pos + int((double+1)/2) if nums[pos] < target else pos - int((double+1)/2)
    #     return self.binary(nums, pos, int((double+1)/2), target)
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo 
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        