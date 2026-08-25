class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1,max(nums)+1):
            if i*k not in nums: return i*k
            if i==max(nums): return (i)+k