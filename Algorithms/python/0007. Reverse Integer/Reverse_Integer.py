class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        reverse = str(sign * x)[::-1]
        #print(sign * int(reverse))
        return sign * int(reverse) * (int(reverse) < 2**31)
        """
        :type x: int
        :rtype: int
        """
        