class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        a,A=[],combinations([1,2,3,4,5,6,7,8,9],k)
        for i in A:
            if sum(i)==n: a.append(i)
        return a