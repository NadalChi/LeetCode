class Solution:
    def letterCombinations(self, digits):
        dict1 = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans = []
        if digits == "":
            return []
        for i in range(0,len(dict1[str(digits[0:1])])):
            ans.append(dict1[str(digits[0:1])][i])
        return self.output(digits,ans,1,dict1)
    def output(self,digits,ans,level,dict1):
        if len(digits) <= level:
            return ans
        else:
            temp = digits[level:level+1]
            
            ans_len = len(ans)
            ans_temp = ans
            for i in range(0,len(dict1[str(temp)])-1):
                ans = ans + ans_temp
            for i in range(0,len(dict1[str(temp)])):
                for j in range(0,ans_len):
                    ans[i*ans_len+j] = ans[i*ans_len+j] + dict1[str(temp)][i]
            level += 1
            return self.output(digits,ans,level,dict1)
        """
        :type digits: str
        :rtype: List[str]
        """
        