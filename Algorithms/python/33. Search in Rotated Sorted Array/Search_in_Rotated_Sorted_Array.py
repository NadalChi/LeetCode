class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while r > l:
            tempr , templ = r, l
            mid = (l + r) // 2
            if target < nums[0] < nums[mid]:
                l = mid + 1
            elif target >= nums[0] > nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid

            else:
                return mid
        return -1