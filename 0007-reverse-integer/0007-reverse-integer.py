class Solution:
    def reverse(self, x: int) -> int:
        n=int(str(abs(x))[::-1])
        if x<0: n*=-1
        if -2**31<=n<=2**31-1: return n
        else: return 0