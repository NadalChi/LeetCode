class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a
        carry = 0
        res = ''
        for i in range(len(a)-1, -1, -1):
            #print(a[i],b[i], carry)
            temp = int(a[i]) + int(b[i]) + carry
            if temp > 1:
                carry = 1
                temp -= 2
            else:
                carry = 0
            res = str(temp) + res
        if carry == 1:
            res = '1' + res
        return res