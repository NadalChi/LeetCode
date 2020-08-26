#from itertools import combinations
class Solution:
    def combine(self, n, k):
        #return list(combinations(range(1, n+1), k))
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        