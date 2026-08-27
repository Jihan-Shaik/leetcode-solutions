class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r,w,b=nums.count(0),nums.count(1),nums.count(2)
        del nums[:]
        for i in range(r):
            nums.append(0)
        for i in range(w):
            nums.append(1)
        for i in range(b):
            nums.append(2)