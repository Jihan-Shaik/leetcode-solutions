class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        C=[]
        for i in nums:
            c=0
            for j in nums:
                if i>j: c+=1
            C.append(c)
        return C