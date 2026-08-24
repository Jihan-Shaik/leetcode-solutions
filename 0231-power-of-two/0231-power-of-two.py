class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n>0 and (int(math.log2(n))==math.log2(n)): return True
        else: return False