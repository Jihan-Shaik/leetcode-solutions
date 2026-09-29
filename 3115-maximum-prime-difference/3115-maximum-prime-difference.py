class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        a,b=0,0
        def prime(n):
            if n==1: return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0: return False
            return True
        for i in range(len(nums)):
            if prime(nums[i]): 
                a=i
                break
        for i in range(len(nums)-1,-1,-1):
            if prime(nums[i]): 
                b=i
                break
        return b-a