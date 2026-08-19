class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        z=set(nums[0])
        for i in nums[1:]: z&=set(i)
        return sorted(list(z))