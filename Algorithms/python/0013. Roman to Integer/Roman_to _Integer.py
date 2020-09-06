class Solution:
    def romanToInt(self, s):
        count = 0 #should use dictionary
        for i in range(len(s)-1,-1,-1):
            if s[i] == 'M':
                count += 1000
            elif s[i] == 'D':
                if count < 1000:
                    count += 500
                else:
                    count -= 500
            elif s[i] == 'C':
                if count < 500:
                    count += 100
                else:
                    count -= 100
            elif s[i] == 'L':
                if count < 100:
                    count += 50
                else:
                    count -= 50
            elif s[i] == 'X':
                if count < 50:
                    count += 10
                else:
                    count -= 10
            elif s[i] == 'V':
                if count < 10:
                    count += 5
                else:
                    count -= 5
            elif s[i] == 'I':
                if count >= 0 and count < 5:
                    count += 1
                else:
                    count -= 1
        return count
        """
        :type s: str
        :rtype: int
        """
        