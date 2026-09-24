class Solution:
    def averageValue(self, nums: list[int]) -> int:
        c,C=0,0
        for i in nums:
            if i%6==0:
                C+=i
                c+=1
        return 0 if c==0 else int(C/c)  