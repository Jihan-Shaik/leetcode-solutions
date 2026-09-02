class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))!=1: num=sum(int(x) for x in " ".join(str(num)).split())
        return num