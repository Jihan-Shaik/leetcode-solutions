class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        import itertools
        num=[a for a in range(1,n+1)]
        return [a for a in combinations(num,k)]