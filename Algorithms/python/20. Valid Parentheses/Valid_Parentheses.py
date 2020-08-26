class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack:
                    return False
                temp = stack.pop()
                if temp != '(':
                    return False
            elif i == ']':
                if not stack:
                    return False
                temp = stack.pop()
                if temp != '[':
                    return False
            elif i == '}':
                if not stack:
                    return False
                temp = stack.pop()
                if temp != '{':
                    return False
        return stack == []
        """
        :type s: str
        :rtype: bool
        """