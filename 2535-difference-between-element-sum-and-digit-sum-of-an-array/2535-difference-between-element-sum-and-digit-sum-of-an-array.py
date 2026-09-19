class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            for j in str(i): c+=int(j)
        return abs(sum(nums)-c)