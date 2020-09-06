class Solution:
    def countAndSay(self, n):
        res = '1'
        for i in  range(n-1):
            temp = ''
            count = 1
            for j in range(len(res)):
                if j == len(res) - 1:
                    temp += str(count) + str(res[-1])
                elif res[j] == res[j + 1]:
                    count += 1
                else:
                    temp += str(count) + str(res[j])
                    count = 1
            res = temp
        return res
        """
        :type n: int
        :rtype: str
        """
        