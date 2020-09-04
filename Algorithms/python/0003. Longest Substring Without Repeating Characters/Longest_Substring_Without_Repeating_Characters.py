class Solution:
    def lengthOfLongestSubstring(self, s):
        res = []
        max_res = []
        for i in s:
            if i not in res:
                res.append(str(i))
            else:
                temp = res.index(i)
                res = res[temp + 1:]
                res.append(i)
            max_res = res if len(res) > len(max_res) else max_res
        #print(max_res)
        return len(max_res)
        """
        :type s: str
        :rtype: int
        """
        