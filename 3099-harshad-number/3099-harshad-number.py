class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=sum([int(a) for a in " ".join(str(x)).split()])
        return s if x%s==0 else -1