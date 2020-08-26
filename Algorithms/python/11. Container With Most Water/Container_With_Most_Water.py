class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_, front, end = min(height[0], height[-1]) * (len(height) - 1), 0, len(height) - 1
        while front < end:
            if height[front] > height[end]:
                end -= 1
            else:
                front += 1
            max_ = max(max_, min(height[front], height[end]) * (end - front))
        return max_