class Solution: 
    def sumOfThree(self, num: int) -> List[int]:
        n=(num-3)/3
        if int(n)==n: return [int(n),int(n+1),int(n+2)]
        else: return []