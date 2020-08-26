class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def Parentheses(n, stack, string):
        #     if n == 0 and not stack:
        #         self.res.append(string)
        #         return
        #     if n > 0:
        #         Parentheses(n - 1, stack + ['('], string + '(')
        #     if stack:
        #         Parentheses(n , stack[:-1], string + ')')
        # self.res = []
        # Parentheses(n, [], '')
        # return self.res
        def Parentheses(n, m, string):
            if n == 0 and m == 0:
                self.res.append(string)
                return
            if n > 0:
                Parentheses(n - 1, m + 1, string + '(')
            if m > 0:
                Parentheses(n , m - 1, string + ')')
        self.res = []
        Parentheses(n, 0, '')
        return self.res