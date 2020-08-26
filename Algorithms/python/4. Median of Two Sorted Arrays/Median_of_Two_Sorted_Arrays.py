class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a = nums1 + nums2
        a.sort()
        return float(a[int(len(a)/2)] + a[int((len(a)/2) - 1)])/2 if len(a) % 2 == 0 else float(a[int((len(a) - 1)/2)])
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        