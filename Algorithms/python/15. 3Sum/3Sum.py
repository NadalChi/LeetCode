class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        nums.sort()
        res = []
        for i in range(len(nums)):
            dict[nums[i]] -= 1
            if i != 0 and nums[i] == nums[i-1]:
                pass
            else:
                for j in range(i+1, len(nums)):
                    if j == i+1 or nums[j] != nums[j - 1]:
                        if nums[j] > -nums[i]/2:
                            break
                        if -(nums[i]+nums[j]) in dict and dict[-(nums[i]+nums[j])]:
                            if nums[j] == -(nums[i]+nums[j]) and dict[-(nums[i]+nums[j])] < 2:
                                pass
                            else:
                                res.append([nums[i], nums[j], -(nums[i]+nums[j])])
        return res
        