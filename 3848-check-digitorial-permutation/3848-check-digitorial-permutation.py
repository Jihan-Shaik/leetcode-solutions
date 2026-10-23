class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        from math import factorial
        c=0
        for i in str(n): c+=factorial(int(i))
        if sorted(str(c))==sorted(str(n)): return True
        return False