class Solution:
    def convertToBase7(self, num: int) -> str:
        r,n,R="",abs(num),num
        while n>=7:
            r+=str(n%7)
            n//=7
        if R>0: return str(n)+r[::-1]
        elif R<0: return "-"+str(n)+r[::-1]
        else: return "0"