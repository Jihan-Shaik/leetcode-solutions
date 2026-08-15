class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        C=nums.count(0)
        for i in range(C):
            nums.remove(0)
            nums.append(0)