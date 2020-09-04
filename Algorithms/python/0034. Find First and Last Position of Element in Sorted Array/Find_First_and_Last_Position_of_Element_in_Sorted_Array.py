class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        head, tail = 0, len(nums) - 1
        index = None
        while head <= tail:
            mid = (head + tail)//2
            if nums[mid] == target:
                index = mid
                break
            if nums[mid] > target:
                tail = mid - 1
            else:
                head = mid + 1
        if index == None:
            return [-1,-1]
        head, tail = 0, index
        while head < tail:
            mid = (head + tail)//2
            if nums[mid] == target:
                tail = max(0, mid - 1)
            else:
                head = mid + 1
        head_index = (head + tail)//2 if nums[(head + tail)//2] == target else (head + tail)//2 + 1
        head, tail = index, len(nums) - 1
        while head < tail:
            mid = (head + tail)//2
            if nums[mid] == target:
                head = min(mid + 1, len(nums) - 1)
            else:
                tail = mid - 1
        tail_index = (head + tail)//2  if nums[(head + tail)//2] == target else (head + tail)//2 - 1
        return [head_index, tail_index]