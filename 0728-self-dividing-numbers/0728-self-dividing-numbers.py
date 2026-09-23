class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        return [a for a in range(left,right+1) if "0" not in str(a) and all(a%int(b)==0 for b in str(a))]