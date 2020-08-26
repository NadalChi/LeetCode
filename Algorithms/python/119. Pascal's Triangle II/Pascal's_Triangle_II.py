res = [[1]]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        while len(res) <= rowIndex:
            temp = []
            for i in range(1,len(res[-1])):
                temp.append(res[-1][i-1]+res[-1][i])
            temp = [1]+temp+[1]
            res.append(temp)
        return res[rowIndex]