class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        max_len = 0
        ans = 0
        for i in range(len(s) - 1):
            k = 1
            temp_len = 1
            while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
                temp_len += 2
                k += 1
            k1 = 1
            temp_len1 = 0
            if s[i] == s[i + 1]:
                temp_len1 = 2
                while i - k1 >= 0 and i + k1 + 1 < len(s) and s[i - k1] == s[i + k1 + 1]:
                    temp_len1 += 2
                    k1 += 1
            if max(temp_len,temp_len1) > max_len:
                max_len = max(temp_len,temp_len1)
                ans = i
        if max_len == 0:
            return s[0]
        return s[ans - int(max_len/2) : ans +  int(max_len/2) + 1] if max_len % 2 == 1 else s[ans - int(max_len/2) + 1 : ans + int(max_len/2) + 1]
        """
        :type s: str
        :rtype: str
        """
        