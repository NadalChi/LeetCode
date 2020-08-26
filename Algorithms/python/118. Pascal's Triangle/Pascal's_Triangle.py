class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            row = []
            row.append(1)
            if i >= 1:
                for j in range(i - 1):
                    row.append(res[i - 1][j] + res[i - 1][j + 1])
                row.append(1)
            res.append(row)
        return res
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        