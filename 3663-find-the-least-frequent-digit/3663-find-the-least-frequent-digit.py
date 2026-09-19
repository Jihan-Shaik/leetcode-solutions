class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s,S=list(set(" ".join(str(n)).split())),[]
        for i in s: S.append([str(n).count(i),int(i)])
        return min(S)[1]