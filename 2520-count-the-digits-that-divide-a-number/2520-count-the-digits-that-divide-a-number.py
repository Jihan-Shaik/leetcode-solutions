class Solution:
    def countDigits(self, num: int) -> int:
        return len([int(a) for a in " ".join(str(num)).split() if int(a)!=0 and num%int(a)==0])