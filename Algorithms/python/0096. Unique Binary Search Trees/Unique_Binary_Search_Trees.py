class Solution:
    def numTrees(self, n: int) -> int:
        dp = (n + 1)* [None]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            temp = 0
            for j in range(0, i):
                temp += (dp[j] * dp[i - j - 1])
            dp[i] = temp
        return dp[n]
        