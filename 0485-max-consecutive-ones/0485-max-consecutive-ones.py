class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c,C=0,0
        for i in nums:
            if i==1: 
                c+=1
                C=max(c,C)
            else: c=0
        return C