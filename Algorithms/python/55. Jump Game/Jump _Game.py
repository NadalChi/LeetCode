class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        end = nums[0]
        while index <= end:
            end = max(end, nums[index] + index)
            if end >= len(nums) - 1:
                return True
            index += 1
        return False