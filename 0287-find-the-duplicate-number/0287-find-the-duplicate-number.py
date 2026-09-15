class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        import statistics
        return statistics.mode(nums)