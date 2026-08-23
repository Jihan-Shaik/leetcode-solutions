class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N=[]
        for i in set(nums):
            N.append([nums.count(i),i])
        return max(N)[-1]