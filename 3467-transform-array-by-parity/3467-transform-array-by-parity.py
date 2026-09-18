class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        c=0
        for i in nums:
            if i%2==0: c+=1
        return [0]*c+[1]*(len(nums)-c)