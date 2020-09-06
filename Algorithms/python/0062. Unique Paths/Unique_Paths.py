#from scipy.special import comb
class Solution:
    def uniquePaths(self, m, n):
        # if m == 1 or n == 1: # use import comb
        #     return 1
        # return int(comb(m + n -2,m -1))
        
        return int(math.factorial(m + n -2)/math.factorial(m - 1)/math.factorial(n - 1)) #with math.factorial
        
        # c = min(m,n)
        # diff = abs(m-n)
        # print(c,diff)
        #ans = (int(comb(2*c,c))-int(comb(2*c,c+1)))*int(comb(diff + c,diff)) #卡塔蘭函數
        
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        