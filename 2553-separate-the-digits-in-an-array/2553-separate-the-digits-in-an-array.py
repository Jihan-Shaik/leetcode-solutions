class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n=[]
        for i in nums: 
            for j in str(i): n.append(int(j))
        return n