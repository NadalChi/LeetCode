class Solution:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        local_min, max, min_, res = prices[0], 0, prices[0], 0
        for i in range(len(prices)):
            if max < prices[i]:
                max = prices[i]
                min_ = min(local_min,min_)
                res = max - min_
            elif prices[i] - local_min > res:
                max = prices[i]
                min_ = local_min
                res = max - min_
            elif min_ > prices[i] and local_min > prices[i]:
                local_min = prices[i]
            #print(local_min, max, min_, res)
        return res
            
        #return max(j - prices[i] for i in range(len(prices)) for j in prices[i:]) #Time Limit Exceeded
        """
        :type prices: List[int]
        :rtype: int
        """
        