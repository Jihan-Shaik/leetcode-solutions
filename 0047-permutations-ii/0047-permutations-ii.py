class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        from itertools import permutations
        return [a for a in set(permutations(nums))]