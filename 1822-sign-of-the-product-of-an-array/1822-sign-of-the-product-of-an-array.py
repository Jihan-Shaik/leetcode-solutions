class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c=1
        def signFunc(x):
            if x>0: return 1
            elif x<0: return -1
            else: return 0
        for i in nums: c*=i
        return signFunc(c)