class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        res = ""
        index = 0
        com = ""
        while index != len(strs[0]):
            if index < len(strs[0]):
                com = strs[0][index]
                for i in strs:
                    if index >= len(i):
                        return res
                    if i[index] != com:
                        return res
                res += str(com)
                index += 1
        return res
        """
        :type strs: List[str]
        :rtype: str
        """
        