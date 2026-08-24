class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if n>0:
            if math.log(n,4).is_integer(): return True
            else: return False
        else: return False