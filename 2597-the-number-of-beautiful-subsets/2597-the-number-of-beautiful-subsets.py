class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        from itertools import combinations
        def beaut(i):
            for a,b in combinations(i,2):
                if abs(a-b)==k: return False
            return True
        n=[]
        for i in range(1,len(nums)+1):
            for j in combinations(nums,i): n.append(j)
        c=0
        for i in n:
            if len(i)==1: c+=1
            elif beaut(i): c+=1
        return c