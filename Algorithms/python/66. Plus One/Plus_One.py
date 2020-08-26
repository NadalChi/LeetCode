class Solution:
    def plusOne(self, digits):
        if not digits:
            return [1]
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] == 10:
                digits [i - 1] += 1
                digits[i] = 0
        if digits[0] == 10:
            digits.insert(0,1)
            digits[1] = 0
        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        