class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0: return True
        elif num==1: return False
        else:
            for i in range(1,num):
                if i+int(str(i)[::-1].lstrip("0"))==num:
                   return True
                   break
        return False