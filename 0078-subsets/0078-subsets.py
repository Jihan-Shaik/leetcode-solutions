class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        from itertools import combinations
        n=[]
        for i in range(len(nums)+1):
            c=combinations(nums,i)
            for j in c: n.append(j)
        return n