class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        c=0
        def prime(n):
            if n<2: return False 
            for i in range(2,int(n**0.5)+1): 
                if n%i==0: return False
            return True
        for i in range(len(nums)):
            if prime(nums[i][i]): c=max(c,nums[i][i])
            if prime(nums[i][len(nums)-i-1]): c=max(c,nums[i][len(nums)-i-1])
        return c