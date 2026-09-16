class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum([a for a in range(1,n+1) if a%m!=0])-sum([a for a in range(1,n+1) if a%m==0])