class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        while intervals:
            front, back = intervals.pop(0)
            while intervals and intervals[0][0] <= back:
                back = max(intervals.pop(0)[1], back)
            res.append([front, back])
        return res