class Solution:
    def merge(self, nums1, m, nums2, n):
        # for i in range(len(nums1)-1, -1, -1): #不考慮m,n
        #     if not nums2:
        #         break
        #     while nums2[-1] > nums1[i]:
        #         nums1.insert(i + 1,nums2[-1])
        #         nums2.pop()
        #         if not nums2:
        #             break
        # while nums2 != []:
        #     nums1.insert(0,nums2[-1])
        #     nums2.pop()
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]    
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        