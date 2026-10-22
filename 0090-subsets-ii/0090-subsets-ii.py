class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        from itertools import combinations
        n=[]
        for i in range(len(nums)+1):
            for j in combinations(nums,i): n.append(tuple(sorted(j)))
        return list(list(a) for a in set(n))