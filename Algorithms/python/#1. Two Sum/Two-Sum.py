class Solution:
    def twoSum(self, nums, target):
        # temp = None
        # for i in range(len(nums)):
        #     #print(nums[i],target - nums[i],nums[i+1:])
        #     if (target - nums[i]) in nums[i+1:] and temp == None:
        #         temp = i
        #     elif temp != None:
        #         if nums[i] == target - nums[temp]:
        #             return(temp, i)
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """