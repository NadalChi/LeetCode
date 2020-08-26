class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            temp = 0
            for k in range(len(needle)):
                if haystack[i+k] == needle[k]:
                    temp += 1
                    if temp == len(needle):
                        return i
                    else:
                        continue
                else:
                    break
        return -1
        #return len(haystack.split(needle)[0]) #用needle當作被split的對象
        
        # if needle not in haystack:
        #         return -1
        # else:
        #     return haystack.index(needle)
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        