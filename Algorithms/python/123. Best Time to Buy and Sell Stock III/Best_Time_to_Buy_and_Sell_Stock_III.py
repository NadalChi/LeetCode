class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2, sale1, sale2 = float('inf'), float('inf'), 0, 0
        for p in prices:
            buy1 = min(buy1, p)
            sale1 = max(sale1, p - buy1)
            buy2 = min(buy2, p - sale1)#max(buy2, sale1 - p)
            sale2 = max(sale2, p - buy2)
        return sale2