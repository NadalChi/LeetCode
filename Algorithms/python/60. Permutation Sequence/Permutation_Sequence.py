class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        t=1
        res = ''
        nums = []
        for i in range(1,n+1):
            nums.append(str(i))
        for i in range(2,n+1):
            t *= i
        for i in range(n,0,-1):
            t /= i
            quotient = int(k / t) if k%t!=0 else int(k/t)-1
            res += nums[quotient]
            k -= (quotient)*t
            nums.pop(quotient)
        return res