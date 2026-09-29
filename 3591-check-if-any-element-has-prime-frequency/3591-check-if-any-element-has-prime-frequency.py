class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def prime(n):
            if n<2: return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0: return False
            return True
        for i in set(nums):
            if prime(nums.count(i)): return True
        return False