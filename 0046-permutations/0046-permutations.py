class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        import itertools
        return [a for a in itertools.permutations(nums)]