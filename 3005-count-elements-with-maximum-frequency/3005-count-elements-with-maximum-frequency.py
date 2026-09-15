class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c,C=0,[nums.count(a) for a in set(nums)]
        for i in set(nums):
            if nums.count(i)==max(C): c+=nums.count(i)
        return c