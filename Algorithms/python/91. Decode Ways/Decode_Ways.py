class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        a = s
        n = len(s)
        if n == 0:
            return 0
        else:
            count = [None]*(n+1)
            count[n] = 1
            count[n-1] = 1 if a[n-1] != '0' else 0
            for i in range(n-2,-1,-1):
                count[i] = 0 if int(a[i:i+1]) == 0 else count[i+1] + count[i+2] if int(a[i:i+2]) <= 26  else count[i+1]
            return count[0]