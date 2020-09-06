class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n//2):
            for j in range(i, m - i - 1):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][m-1-j], matrix[m-1-j][i] = matrix[m-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][m-1-j]