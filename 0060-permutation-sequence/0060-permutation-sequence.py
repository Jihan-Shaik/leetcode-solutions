class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        return "".join(str(a) for a in list(permutations(range(1,n+1)))[k-1])