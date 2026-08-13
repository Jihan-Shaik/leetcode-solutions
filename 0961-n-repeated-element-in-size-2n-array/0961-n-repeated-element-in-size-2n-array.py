class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return next(x for x in nums if nums.count(x)==len(nums)/2)